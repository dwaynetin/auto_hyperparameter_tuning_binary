import unittest
import os
from src.transformer.index_analyzer import index_analyzer
import pandas as pd

class index_analyzer_tests(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({"letter1": ["a","d","g"], "letter2": ["b","e","h"], "letter3": ["c","f","i"]})
        self.sample_data_with_index = pd.DataFrame({"random": ['1','2','3'], "letter1": ["a","d","g"], "letter2": ["b","e","h"], "letter3": ["c","f","i"]})
        self.sample_data_with_fake_index = pd.DataFrame({"random": ['1','4','3'], "letter1": ["a","d","g"], "letter2": ["b","e","h"], "letter3": ["c","f","i"]})
        self.index_analyzer = index_analyzer()

    def test_should_not_find_index(self):
        self.assertEquals(self.index_analyzer.find_index_column(self.sample_data), "")

    def test_should_not_find_index_when_index_is_fake(self):
        self.assertEquals(self.index_analyzer.find_index_column(self.sample_data_with_fake_index), "")

    def test_should_find_index_when_data_is_correct(self):
        self.assertEquals(self.index_analyzer.find_index_column(self.sample_data_with_index), "random")