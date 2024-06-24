"""
Train our Tokenizers on some data, just to see them in action.
The whole thing runs in ~25 seconds on my laptop.
"""

import os
import time
import argparse
from language_bpe import BPETokenizer

parser = argparse.ArgumentParser(prog="BPE Tokenizer")
parser.add_argument("--input_file", default="data/hindi.txt", type=str)
parser.add_argument("--output_file", default="tokenizer", type=str)
parser.add_argument("--vocab_size", default=500, type=int)
args = parser.parse_args()


# open some text and train a vocab of 512 tokens
text = open(args.input_file, "r", encoding="utf-8").read()

# create a directory for models, so we don't pollute the current directory
os.makedirs("models", exist_ok=True)

t0 = time.time()
# construct the Tokenizer object and kick off verbose training
tokenizer = BPETokenizer()
tokenizer.build(text, args.vocab_size, verbose=True)
# writes two files in the models directory: name.model, and name.vocab
prefix = os.path.join("models", args.output_file)
tokenizer.save(prefix)
t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")