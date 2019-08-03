from src.utilities.abstract_parser import abstract_parser

class classifier_parser(abstract_parser):
    def __init__(self):
        abstract_parser()
    def parse(self, filename):
        parser = self.retrieve_parser(filename)
        parsed_configuration = {}
        for section_name in parser.sections():
            parsed_entry = {}
            classifier_name = ""
            for name, value in parser.items(section_name):
                if name == "name":
                    classifier_name = value
                elif "_list_" in name:
                    temporary_list = value.split(',')
                    parsed_entry["classifier__"+name[6:]] = self.__identify_list_dtype(temporary_list)
                else:
                    parsed_entry["classifier__"+name] = value
            parsed_configuration[classifier_name] = parsed_entry
        return parsed_configuration

    def __identify_list_dtype(self, list_to_check):
        print list_to_check
        if all(self.__is_float(x) for x in list_to_check) == True:
            if all(self.__is_without_period(x) for x in list_to_check) == True:
                return [int(x) for x in list_to_check]
            else:
                return [float(x) for x in list_to_check]
        else:
            return list_to_check

    def __is_float(self,text):
        try:
            float(text)
            return True
        except ValueError:
            return False

    def __is_without_period(self,text):
        try:
            text.index(".")
            return False
        except ValueError:
            return True