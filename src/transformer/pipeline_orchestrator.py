from sklearn.pipeline  import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV

class pipeline_orchestrator:
    def __init__(self, classifier_hyperparameter_generator, classifier_hp_pairs):
        self.classifier_hp_pairs = classifier_hp_pairs
        self.classifier_hp_generator = classifier_hyperparameter_generator

    def train(self, training_data, training_result_data):
        training_details = []
        for key in self.classifier_hp_pairs.keys():
            print "current classifier is " + key
            print self.classifier_hp_pairs[key]
            steps = [('imputation', Imputer(missing_values='NaN', strategy = 'most_frequent', axis=0)), ('classifier', self.classifier_hp_generator.convert(key))]
            pipeline = Pipeline(steps)
            classifier_score, best_score = self.__apply_grid_search_cv_to_pipeline(pipeline, self.classifier_hp_pairs[key] , training_data, training_result_data)
            training_details.append({'clf': key, 'params': classifier_score, 'score': best_score})
        return sorted(training_details, key=lambda training_detail: training_detail['score'])

    def __apply_grid_search_cv_to_pipeline(self, pipeline, hyperparameters, training_data, training_result_data):
        kfold = KFold(n_splits=10, random_state=42)
        grid_search_clf = GridSearchCV(pipeline, hyperparameters, cv=kfold, scoring={"AUC":"roc_auc"}, refit="AUC")
        grid_search_clf.fit(training_data, training_result_data)
        return grid_search_clf.best_params_, grid_search_clf.best_score_
    # Create the user of orchestration (Thanos)
    # Create a main class that orchestrates the whole flow, creates Thanos