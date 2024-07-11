# Workshop SPARE_SCORES Model Training & Testing

This project involves training and testing a SPARE_SCORES model using the SPARE framework. The provided CLI tool allows users to easily train a model on a given dataset and test it on another dataset.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [CLI Arguments](#cli-arguments)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/iSTAGING_Workshop.git
    cd iSTAGING_Workshop
    ```

2. **Create a virtual environment:**

    ```sh
    conda create -n workshop python=3.8
    conda activate workshop
    ```

3. **Install the dependencies:**

    ```sh
    pip install numpy pandas scikit-learn spare-scores
    ```

## Usage

The CLI tool supports both training and testing modes. It can be invoked as follows:

1. **Training:**
    ```sh
    python iSTAGING_Workshop/cli.py --action train --input path/to/train_data.csv --output path/to/save_model.pkl.gz
    ```

2. **Testing:**
    ```
    python iSTAGING_Workshop/cli.py --action test --input path/to/test_data.csv --model path/to/saved_model.pkl.gz --output path/to/save_results.csv
    ```

## CLI arguments

### Required CLI arguments

- `-a, --action`: The action to be performed, either train or test.
- `-i, --input`: The dataset to be used for training/testing, provided as a CSV file.

### Optional Arguments

- `-m, --model, --model_file`: The model file to be used for testing. Required for testing.
- `-o, --output`: The filename for the model to be saved (if training) or the test results to be saved (if testing).
- `-h, --help`: Show the help message and exit.
- `-V, --version`: Display the version of the package.

## Examples

1. **Training a Model**

    To train a model with the provided training dataset:

    ```sh
    python cli.py --action train --input data/train_data.csv --output my_model.pkl.gz
    ```

2. **Testing a Model**

    To test the provided model:

    ```sh
    python cli.py --action test --input test_data.csv --model model/test.pkl.gz --output predictions.csv
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Check out the [CONTRIBUTING.md](CONTRIBUTING.md) for more info! Also check out the [Code of Conduct](CODE_OF_CONDUCT.md) of the project.

## License

This project is licensed under the CBICA License - see the [LICENSE](LICENSE) file for details.

## References

- SPARE-AD

  Davatzikos, C., Xu, F., An, Y., Fan, Y. & Resnick, S. M. Longitudinal progression of Alzheimer's-like patterns of atrophy in normal older adults: the SPARE-AD index. Brain 132, 2026-2035, [doi:10.1093/brain/awp091](https://doi.org/10.1093/brain/awp091) (2009).
    ```bibtex
        @article{davatzikos2009sparead,
            title={Longitudinal progression of Alzheimer's-like patterns of atrophy in normal older adults: the SPARE-AD index},
            author={Davatzikos, Christos and Xu, Feng and An, Yaakov and Fan, Yong and Resnick, Susan M},
            journal={Brain},
            volume={132},
            pages={2026--2035},
            year={2009},
            publisher={Oxford University Press},
            doi={10.1093/brain/awp091}
        }
    ```

- SPARE-BA

  Habes, M. et al. Advanced brain aging: relationship with epidemiologic and genetic risk factors, and overlap with Alzheimer disease atrophy patterns. Transl Psychiatry 6, e775, [doi:10.1038/tp.2016.39](https://doi.org/10.1038/tp.2016.39) (2016).
    ```bibtex
        @article{habes2016spareba,
        title={Advanced brain aging: relationship with epidemiologic and genetic risk factors, and overlap with Alzheimer disease atrophy patterns},
        author={Habes, Mollie and others},
        journal={Translational Psychiatry},
        volume={6},
        pages={e775},
        year={2016},
        publisher={Nature Publishing Group},
        doi={10.1038/tp.2016.39}
        }
    ```

- diSPARE-AD

  Hwang, G. et al. Disentangling Alzheimer's disease neurodegeneration from typical brain ageing using machine learning. Brain Commun 4, fcac117, [doi:10.1093/braincomms/fcac117](https://doi.org/10.1093/braincomms/fcac117) (2022).
  ```bibtex
        @article{hwang2022disparead,
        title={Disentangling Alzheimer's disease neurodegeneration from typical brain ageing using machine learning},
        author={Hwang, Gabriel and others},
        journal={Brain Communications},
        volume={4},
        pages={fcac117},
        year={2022},
        publisher={Oxford University Press},
        doi={10.1093/braincomms/fcac117}
        }
    ```

## Disclaimer

- The software has been designed for research purposes only and has neither been reviewed nor approved for clinical use by the Food and Drug Administration (FDA) or by any other federal/state agency.

## Contact

For more information and support, please contact [aidinisg@pennmedicine.upenn.edu](mailto:aidinisg@pennmedicine.upenn.edu).