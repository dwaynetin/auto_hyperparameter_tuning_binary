class classifier_hyperparameter_pair_generator:
    def convert(self, classifier):
        parts = classifier.rsplit(".", 1)
        module = __import__(parts[0], fromlist=[parts[1]])
        reflected_class = getattr(module, parts[1])
        return reflected_class()