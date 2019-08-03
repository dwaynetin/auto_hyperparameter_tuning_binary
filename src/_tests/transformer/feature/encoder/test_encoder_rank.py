import unittest
import pandas as pd
import numpy as np
from src.transformer.feature.encoder.encoder_rank import encoder_rank

class encoder_rank_tests(unittest.TestCase):
    def test_should_rank_numbers(self):
        # given
        test_data = pd.DataFrame({"ranking": [4, 8, 10, 3, 12]})

        # then
        encoded_df = encoder_rank("ranking", test_data, {4:1, 8:2, 10:3, 3:4, 12:5}).encode()
        np.testing.assert_array_equal(encoded_df.loc[0, "encoded_ranking"], 1.0)
        np.testing.assert_array_equal(encoded_df.loc[1, "encoded_ranking"], 2.0)
        np.testing.assert_array_equal(encoded_df.loc[2, "encoded_ranking"], 3.0)
        np.testing.assert_array_equal(encoded_df.loc[3, "encoded_ranking"], 4.0)
        np.testing.assert_array_equal(encoded_df.loc[4, "encoded_ranking"], 5.0)

    def test_should_rank_alphabet(self):
        # given
        test_data = pd.DataFrame({"ranking": ["completely disagree", "partially disagree", "neutral", "partially agree", "completely agree"]})

        # then
        encoded_df = encoder_rank("ranking", test_data, {"completely disagree":1, "partially disagree":2, "neutral":3, "partially agree":4, "completely agree":5}).encode()
        np.testing.assert_array_equal(encoded_df.loc[0, "encoded_ranking"], 1.0)
        np.testing.assert_array_equal(encoded_df.loc[1, "encoded_ranking"], 2.0)
        np.testing.assert_array_equal(encoded_df.loc[2, "encoded_ranking"], 3.0)
        np.testing.assert_array_equal(encoded_df.loc[3, "encoded_ranking"], 4.0)
        np.testing.assert_array_equal(encoded_df.loc[4, "encoded_ranking"], 5.0)

    def test_should_rank_range(self):
        # given
        test_data = pd.DataFrame({"ranking": [25, 29, 10, 12, 4]})
        test_details = {xrange(1,11):1, xrange(11,21):2, xrange(21,31):3}

        # then
        encoded_df = encoder_rank("ranking", test_data, test_details).encode()
        np.testing.assert_array_equal(encoded_df.loc[0, "encoded_ranking"], 3)
        np.testing.assert_array_equal(encoded_df.loc[1, "encoded_ranking"], 3)
        np.testing.assert_array_equal(encoded_df.loc[2, "encoded_ranking"], 1)
        np.testing.assert_array_equal(encoded_df.loc[3, "encoded_ranking"], 2)
        np.testing.assert_array_equal(encoded_df.loc[4, "encoded_ranking"], 1)