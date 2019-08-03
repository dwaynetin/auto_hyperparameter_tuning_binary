import unittest
from src.transformer.train_test_builder import train_test_builder
import pandas as pd
from mock import Mock
from mock import MagicMock

class ProductionClass:
    def __init__(self):
        pass
    def find_index_column(self, any_val):
        raise NotImplemented

class train_test_builder_tests(unittest.TestCase):
    def test_should_split_dataset_based_on_criterion_no_index_column(self):
        # given
        test_data = pd.DataFrame({"letter1": ["a","d","g"], "letter2": ["b","e","h"], "letter3": ["c","f","i"]})

        # when
        mock_index_analyzer = ProductionClass()
        mock_index_analyzer.find_index_column = MagicMock(return_value="")
        builder = train_test_builder(mock_index_analyzer)

        # then
        question, result = builder.split(test_data,"letter3", ["letter2"])
        self.assertEquals(result["letter3"].tolist(), test_data["letter3"].tolist())
        self.assertEquals(question["letter1"].tolist(), test_data["letter1"].tolist())
        self.assertEquals(question["index"].tolist(), [0,1,2])
        with self.assertRaises(KeyError):
            question["letter2"].tolist()

    def test_should_split_dataset_based_on_criterion_with_index_column(self):
        # given
        test_data = pd.DataFrame({"column": [0,1,2] ,"letter1": ["a","d","g"], "letter2": ["b","e","h"], "letter3": ["c","f","i"]})

        # when
        mock_index_analyzer = ProductionClass()
        mock_index_analyzer.find_index_column = MagicMock(return_value="column")
        builder = train_test_builder(mock_index_analyzer)

        # then
        question, result = builder.split(test_data,"letter3", ["letter2"])
        self.assertEquals(result["letter3"].tolist(), test_data["letter3"].tolist())
        self.assertEquals(question["letter1"].tolist(), test_data["letter1"].tolist())
        self.assertEquals(question["column"].tolist(), test_data["column"].tolist())
        with self.assertRaises(KeyError):
            question["letter2"].tolist()

    def test_should_split_dataset_based_on_criterion_with_index_column_when_retained_all_columns(self):
        # given
        test_data = pd.DataFrame({"column": [0,1,2] ,"letter1": ["a","d","g"], "letter2": ["b","e","h"], "letter3": ["c","f","i"]})

        # when
        mock_index_analyzer = ProductionClass()
        mock_index_analyzer.find_index_column = MagicMock(return_value="column")
        builder = train_test_builder(mock_index_analyzer)

        # then
        question, result = builder.split(test_data,"letter3")
        self.assertEquals(result["letter3"].tolist(), test_data["letter3"].tolist())
        self.assertEquals(question["letter1"].tolist(), test_data["letter1"].tolist())
        self.assertEquals(question["letter2"].tolist(), test_data["letter2"].tolist())
        self.assertEquals(question["column"].tolist(), test_data["column"].tolist())