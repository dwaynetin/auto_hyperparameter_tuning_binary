class encoder_abstract(object):
    def __init__(self, column_name, dataset, column_details={}):
        self.column_name = column_name
        self.dataset = dataset
        self.column_details = column_details

    @staticmethod
    def is_encoder(self, column_type):
        raise NotImplementedError

    def encode(self):
        raise NotImplementedError