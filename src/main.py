import sys
from retriever.dataset_retriever import dataset_retriever
from transformer.index_analyzer import index_analyzer
from transformer.train_test_builder import train_test_builder
from transformer.pipeline_orchestrator import pipeline_orchestrator
from classifiers.classifier_hyperparameter_pair_generator import classifier_hyperparameter_pair_generator
from utilities.classifier_parser import classifier_parser

def main():
    args = sys.argv[1:]
    removed_columns = args[3:]
    dataset = dataset_retriever().retrieve(args[0])
    training_data, test_data = train_test_builder(index_analyzer()).split(dataset, args[2], removed_columns)
    classifier_hp_pairs = classifier_parser().parse(args[1])
    print classifier_hp_pairs
    print pipeline_orchestrator(classifier_hyperparameter_pair_generator(), classifier_hp_pairs).train(training_data, test_data)


if __name__ == "__main__":
    main()