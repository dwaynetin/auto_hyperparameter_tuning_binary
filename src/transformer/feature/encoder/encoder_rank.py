from sklearn.preprocessing import LabelEncoder
import pandas as pd
from src.transformer.feature.encoder.encoder_abstract import encoder_abstract

class encoder_rank(encoder_abstract):
    def __init__(self, column_name, dataset, column_details={}):
        encoder_abstract.__init__(self, column_name, dataset, column_details)
        self.label_encoder = LabelEncoder()

    @staticmethod
    def is_encoder(self, column_type):
        return column_type == "categorize"

    def encode(self):
        # column_details = {'Gen 1': 1, 'Gen 2': 2, 'Gen 3': 3, 'Gen 4': 4, 'Gen 5': 5, 'Gen 6': 6}
        # if range was provided, then this should map as range
        if all(type(key) == xrange for key in self.column_details.keys()) == True:
            x = self.dataset[self.column_name].map(lambda item: self.__check_range(item))
            return pd.DataFrame(x.tolist(), columns=["encoded_" + self.column_name])
        else:
            return pd.DataFrame(self.dataset[self.column_name].map(self.column_details).tolist(), columns=["encoded_" + self.column_name])

    def __check_range(self, item):
        for range_values, rank in self.column_details.items():
            if item in range_values:
                return rank