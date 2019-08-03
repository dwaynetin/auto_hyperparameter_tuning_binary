from src.utilities.feature_parser import feature_parser

class feature_builder:
    def __init__(self, feature_organizer, feature_parser):
        pass
    def convert(self, dataset):
        # feature_parser returns set of columns to convert
        # next, we need to convert the features via encoding, 
        # create an encoder_factory that will identify the needed encoders. should I run the factory on runtime?
        # the encoder factory returns the parsed dataframe
        # feature_organizer will be responsible for appending the data correctly based on the provided columns

        pass