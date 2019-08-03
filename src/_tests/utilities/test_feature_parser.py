import unittest
from src.utilities.feature_parser import feature_parser

class feature_parser_tests(unittest.TestCase):
    def test_should_parse_single_config_correctly(self):
        # given
        parsed_config = feature_parser().parse('src/_tests/assets/sample_feature_config.conf')

        # then
        self.assertEquals(parsed_config[0]["column_name"], "column1")
        self.assertEquals(parsed_config[0]["column_type"], "rank")
        self.assertEquals(parsed_config[1]["column_name"], "column2")
        self.assertEquals(parsed_config[1]["column_type"], "categorize")