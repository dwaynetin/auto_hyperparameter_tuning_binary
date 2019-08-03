import unittest
import pandas as pd
from src.retriever.dataset_retriever import dataset_retriever

class dataset_retriever_tests(unittest.TestCase):
    def setUp(self):
        self.retriever = dataset_retriever()
    def test_should_raise_error_when_retrieving_absent_file(self):
        with self.assertRaises(IOError):
            self.retriever.retrieve("")
    def test_should_return_error_when_retrieving_empty_data(self):
        with self.assertRaises(pd.errors.EmptyDataError):
            self.retriever.retrieve("src/_tests/assets/empty.csv")
    def test_should_return_file_when_retrieving_correct_data(self):
        data = self.retriever.retrieve("src/_tests/assets/sample.csv")
        self.assertIsNotNone(data)