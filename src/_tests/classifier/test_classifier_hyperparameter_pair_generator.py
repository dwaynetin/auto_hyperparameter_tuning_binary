import unittest
from sklearn.neighbors import KNeighborsClassifier
from src.classifiers.classifier_hyperparameter_pair_generator import classifier_hyperparameter_pair_generator

class classifier_parser_tests(unittest.TestCase):
    def test_should_reflect_provided_class_correctly(self):
        # given
        classifier = "sklearn.neighbors.KNeighborsClassifier"

        # then
        resulting_kv_pair = classifier_hyperparameter_pair_generator().convert(classifier)
        print resulting_kv_pair
        self.assertEquals(str(resulting_kv_pair), str(KNeighborsClassifier()))

    def test_should_not_reflect_provided_class_correctly(self):
        # given
        classifier = "x.y"

        # then
        with self.assertRaises(ImportError):
            classifier_hyperparameter_pair_generator().convert(classifier)