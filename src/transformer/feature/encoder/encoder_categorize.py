from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from src.transformer.feature.encoder.encoder_abstract import encoder_abstract

class encoder_categorize(encoder_abstract):
    def __init__(self, column_name, dataset, column_details=[]):
        encoder_abstract.__init__(self, column_name, dataset)
        self.label_encoder = LabelEncoder()
        self.column_transposer = OneHotEncoder()

    @staticmethod
    def is_encoder(self, column_type):
        return column_type == "rank"

    def encode(self):
        feature_raw = self.dataset[self.column_name]
        feature_processing = self.label_encoder.fit_transform(feature_raw)
        self.dataset["encoded_" + self.column_name] = feature_processing
        return self.__transpose()

    def __transpose(self):
        transposed_data = self.column_transposer.fit_transform(self.dataset[["encoded_" + self.column_name]]).toarray()
        transposed_column_names = [(lambda x: "encoded_" + x)(x) for x in list(self.label_encoder.classes_)]
        return pd.DataFrame(transposed_data, columns=transposed_column_names)