import unittest
import pandas as pd
import numpy as np
from src.transformer.feature.encoder.encoder_categorize import encoder_categorize

class encoder_categorize_tests(unittest.TestCase):
    def test_should_categorize_alphabet(self):
        # given
        test_data = pd.DataFrame({"letter1": ["a","d","g"], "letter2": ["b","e","h"], "letter3": ["c","f","i"]})

        # then
        encoded_df = encoder_categorize("letter3", test_data).encode()
        encoded_cfi_names = ["encoded_c", "encoded_f", "encoded_i"]
        np.testing.assert_array_equal(encoded_df.loc[0, encoded_cfi_names], [1.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[1, encoded_cfi_names], [0.0,1.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[2, encoded_cfi_names], [0.0,0.0,1.0])

    def test_should_categorize_alphanumeric(self):
        # given
        test_data = pd.DataFrame({"letter3": ["c","f","i","a2","b3","12"]})

        # then
        encoded_df = encoder_categorize("letter3", test_data).encode()
        encoded_cfi_names = ["encoded_c", "encoded_f", "encoded_i","encoded_a2","encoded_b3","encoded_12"]
        np.testing.assert_array_equal(encoded_df.loc[0, encoded_cfi_names], [1.0,0.0,0.0,0.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[1, encoded_cfi_names], [0.0,1.0,0.0,0.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[2, encoded_cfi_names], [0.0,0.0,1.0,0.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[3, encoded_cfi_names], [0.0,0.0,0.0,1.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[4, encoded_cfi_names], [0.0,0.0,0.0,0.0,1.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[5, encoded_cfi_names], [0.0,0.0,0.0,0.0,0.0,1.0])

    def test_should_categorize_duplicates(self):
        # given
        test_data = pd.DataFrame({"letter3": ["c","f","i","a2","i","12"]})

        # then
        encoded_df = encoder_categorize("letter3", test_data).encode()
        encoded_cfi_names = ["encoded_c", "encoded_f", "encoded_i","encoded_a2","encoded_12"]
        np.testing.assert_array_equal(encoded_df.loc[0, encoded_cfi_names], [1.0,0.0,0.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[1, encoded_cfi_names], [0.0,1.0,0.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[2, encoded_cfi_names], [0.0,0.0,1.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[3, encoded_cfi_names], [0.0,0.0,0.0,1.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[4, encoded_cfi_names], [0.0,0.0,1.0,0.0,0.0])
        np.testing.assert_array_equal(encoded_df.loc[5, encoded_cfi_names], [0.0,0.0,0.0,0.0,1.0])