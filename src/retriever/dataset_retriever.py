import os
import pandas as pd

#Utility class responsible for retrieving data from an external source
class dataset_retriever:
    def retrieve(self, file_path):
        return pd.read_csv(file_path)