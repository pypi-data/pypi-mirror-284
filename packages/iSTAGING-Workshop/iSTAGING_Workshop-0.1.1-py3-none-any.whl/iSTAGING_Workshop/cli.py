import argparse
import pandas as pd
import spare_scores as sp

VERSION = "0.1.0"

from train_test_model import model_train, model_test

def main():
    prog = "spare_scores_model"
    description = "Workshop SPARE_SCORES model training & testing"
    usage = f"""
    {prog} v{VERSION}.
    Workshop SPARE_SCORES model training & testing.

    required arguments:
        [ACTION]        The action to be performed, either 'train' or 'test'
        [-a, --action]

        [INPUT]         The dataset to be used for training / testing. Can be 
        [-i, --input]   a filepath string of a .csv file.

    optional arguments:
        [MODEL]         The model to be used (only) for testing. Can be a 
        [-m, --model,   filepath string of a .pkl.gz file. Required for testing
        --model_file]

        [OUTPUT]        The filename for the model (as a .pkl.gz) to be saved 
        [-o, --output]  at, if training. If testing, the filepath of the 
                        resulting predictions (as a .csv file) to be 
                        saved. If not given, nothing will be saved.

        [HELP]          Show this help message and exit.
        [-h, --help]

        [VERSION]       Display the version of the package.
        [-V, --version]
    """.format(VERSION=VERSION)

    parser = argparse.ArgumentParser(prog=prog,
                                     usage=usage,
                                     description=description,
                                     add_help=False)

    # ACTION argument
    help = "The action to be performed, either 'train' or 'test'"
    parser.add_argument("-a",
                        "--action",
                        type=str,
                        help=help,
                        choices=['train', 'test'],
                        default=None,
                        required=True)

    # INPUT argument
    help = "The dataset to be used for training / testing. Can be a filepath string of a .csv file."
    parser.add_argument("-i",
                        "--input",
                        type=str,
                        help=help,
                        default=None,
                        required=True)

    # MODEL argument
    help = "The model to be used (only) for testing. Can be a filepath string of a .pkl.gz file. Required for testing."
    parser.add_argument("-m",
                        "--model",
                        "--model_file",
                        type=str,
                        help=help,
                        default='model.pkl.gz',
                        required=False)

    # OUTPUT argument
    help = "The filename for the model (as a .pkl.gz) to be saved at, if training. If testing, the filepath of the resulting predictions (as a .csv file) to be saved. If not given, nothing will be saved."
    parser.add_argument("-o",
                        "--output",
                        type=str,
                        help=help,
                        default=None,
                        required=False)

    # HELP argument
    help = 'Show this message and exit'
    parser.add_argument('-h',
                        '--help',
                        action='store_true',
                        help=help)

    # VERSION argument
    help = "Show the version and exit"
    parser.add_argument("-V",
                        "--version",
                        action='version',
                        version=prog + ": v{VERSION}.".format(VERSION=VERSION),
                        help=help)

    args = parser.parse_args()

    if args.action == 'train':
        results = model_train(args.input, args.output)
        print("Model trained and saved.")
        print(results)

    elif args.action == 'test':
        if args.model is None:
            print(usage)
            print("The following argument is required: -m/--model/--model_file")
            return

        results = model_test(args.input, args.model, args.output)
        print("Model tested.")
        if args.output:
            print(f"Results saved to {args.output}")
        else:
            print(results)

if __name__ == '__main__':
    main()