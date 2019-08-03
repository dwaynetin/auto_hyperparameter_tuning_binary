from ConfigParser import SafeConfigParser

class abstract_parser:
    def retrieve_parser(self, filename):
        parser = SafeConfigParser()
        parser.read(filename)
        return parser

    def parse(self, filename):
        raise NotImplementedError