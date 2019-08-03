import unittest
from src.utilities.classifier_parser import classifier_parser

class classifier_parser_tests(unittest.TestCase):
    def test_should_parse_single_config_correctly(self):
        # given
        parsed_config = classifier_parser().parse('src/_tests/assets/sample_config.conf')

        # then
        self.assertEquals(parsed_config['hello']['classifier__address'], 'united states')
        self.assertEquals(parsed_config['hello']['classifier__age'], '23')
        self.assertEquals(parsed_config['hello']['classifier__magic_numbers'], [1,2,3])
        self.assertEquals(parsed_config['hello']['classifier__magic_numbers2'], [1.1,2,3])
        self.assertEquals(type(parsed_config['hello']['classifier__magic_numbers2'][0]), type(1.1))

    def test_should_parse_multiple_config_correctly(self):
        # given
        parsed_config = classifier_parser().parse('src/_tests/assets/sample_config_multiple.conf')

        # then
        self.assertEquals(parsed_config['hello']['classifier__address'], 'united states')
        self.assertEquals(parsed_config['hello']['classifier__age'], '23')
        self.assertEquals(parsed_config['hello']['classifier__magic_numbers'], [1,2,3])
        self.assertEquals(parsed_config['hi']['classifier__address'], 'china')
        self.assertEquals(parsed_config['hi']['classifier__age'], '17')
        self.assertEquals(parsed_config['hi']['classifier__fruits'], ["carrot","orange","apple"])