from src.utilities.abstract_parser import abstract_parser

class feature_parser(abstract_parser):
    def parse(self, filename):
        parser = self.retrieve_parser(filename)
        parsed_configuration = []
        for section_name in parser.sections():
            parsed_entry = {}
            for name, value in parser.items(section_name):
                parsed_entry[name] = value
            parsed_configuration.append(parsed_entry)
        return parsed_configuration