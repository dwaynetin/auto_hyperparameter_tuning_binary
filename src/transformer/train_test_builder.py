from sklearn.model_selection import train_test_split

class train_test_builder:
    def __init__(self, index_analyzer):
        self.analyzer = index_analyzer

    # analyzes the provided dataset for any indexes, and then adds an index if none found. Afterwhich, the dataset is split based on the provided result column
    # returns two values: 1st contains your training data, 2nd contains your results
    def split(self, dataset, result_column, columns_to_remove = []):
        index_column = self.analyzer.find_index_column(dataset)
        if index_column == "":
            return self.__split_data_result_column(dataset.reset_index(), result_column, columns_to_remove)
        else:
            return self.__split_data_result_column(dataset, result_column, columns_to_remove)

    def __split_data_result_column(self, dataset, result_column, columns_to_remove = []):
        columns_to_remove.append(result_column)
        return dataset.loc[:, dataset.columns.difference(columns_to_remove)], dataset.loc[:, dataset.columns == result_column]