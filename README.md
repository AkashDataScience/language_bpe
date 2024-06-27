[![LinkedIn][linkedin-shield]][linkedin-url]

## :jigsaw: Objective

- Collect data of any indian language
- Build a regex for that language
- Build BPE tokenizer for that language

## Prerequisites
* [![Python][Python.py]][python-url]

## :open_file_folder: Files
- [**data**](data/)
    - Folder containing data of Hindi and English Languages
- [**regex_description.ipynb**](regex_description.ipynb)
    - This files contains explaination of GPT-4 regex
    - It also contains explaination of Hindi regex used for this project
- [**base.py**](language_bpe/base.py)
    - Base class for tokenizer
- [**bpe_tokenizer.py**](language_bpe/bpe_tokenizer.py)
    - Class for BPE tokenizer
- [**train.py**](train.py)
    - This is the main file of this project.
    - It uses functions available in `base.py` and `bpe_tokenize.py`.
    - Regex for hindi language is available in this file


## Installation

1. Clone the repo
```
git clone https://github.com/AkashDataScience/language_bpe.git
```
2. Go inside folder
```
 cd language_bpe
```
3. Install dependencies
```
pip install -r requirements.txt
```

## Build tokenizer
1. Collect text data of desired language(s).
2. Write regex for that language by following [regex_description.ipynb](regex_description.ipynb)
3. Build tokenizer

```
# Start building with:
python train.py

# To Build english tokenizer
python train.py --input_file="data/english.txt" --output_file="english_5000" --is_english

# To build hindi tokenizer with 5000 tokens from jupyter notebook
%run train.py --input_file="data/hindi.txt" --output_file="hindi_5000" --vocab_size=5000
```

## Usage 
Please refer to [ERA V2 Session 20](https://github.com/AkashDataScience/ERA-V2/tree/master/Week-20)

## Contact

Akash Shah - akashmshah19@gmail.com  
Project Link - [ERA V2](https://github.com/AkashDataScience/ERA-V2/tree/master)

## Acknowledgments
This repo is developed using references listed below:
* [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
* [Taylor Swift wikipedia page for English data](https://en.wikipedia.org/wiki/Taylor_Swift)
* [OPUS CORPUS for Hindi data](https://opus.nlpl.eu/)

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/akash-m-shah/
[Python.py]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
[PyTorch.tensor]: https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white
[torch-url]: https://pytorch.org/
[HuggingFace.transformers]: https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-orange
[huggingface-url]: https://huggingface.co/