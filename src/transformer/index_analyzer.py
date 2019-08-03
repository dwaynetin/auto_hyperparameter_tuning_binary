import traceback
import pandas as pd

class index_analyzer:
    def find_index_column(self, dataset):
        for key in dataset.keys():
            try:
                numeric_column = pd.to_numeric(dataset[key])
                is_an_iterator = self.__is_column_in_numeric_sequence(numeric_column)
                # print "returned by iterator check is " + str(is_an_iterator)
                if is_an_iterator == True:
                    return key
            except:
                pass
        return ""

    def __is_column_in_numeric_sequence(self, column_data):
            if column_data[0] == 0 or column_data[0] == 1:
                prev_num = column_data[0]
                for single_cell in column_data[1:]:
                    # print "CURRENTLY CHECKING " + str(prev_num) + str(single_cell)
                    if single_cell - prev_num == 1:
                        prev_num = single_cell
                    else:
                        return False
                return True
            else:
                return False