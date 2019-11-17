import os
import subprocess
from argparse import ArgumentParser
from bert_serving.client import BertClient

import settings

parser = ArgumentParser()
parser.add_argument('input_files', nargs='+')
args = parser.parse_args()

bert_client = BertClient(ip='bert-server', ignore_all_checks=True)

def grep_input_file(pattern, input_file):
    command = ['grep', '-iw', '-m', settings.MAX_SENTENCES_PER_FILE, pattern, input_file]
    output = subprocess.check_output(command).decode('utf-8')
    return output.strip().split('\n')

def get_sentences(pattern):
    filename_sentence_pairs = []

    for input_file in args.input_files:
        matches = grep_input_file(pattern, input_file)
        filename_sentence_pairs += [(input_file, match) for match in matches]

    return filename_sentence_pairs

def get_encodings(sentences):
    encodings = bert_client.encode(sentences)
    return encodings