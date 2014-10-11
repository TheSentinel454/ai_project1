from __future__ import division
from os import listdir
from os.path import isfile, join
import numpy as np

data_path = './mq-public/CHI_MQ_Data/Dell Data/'

def get_subdirs(path):
    return [join(path,f) for f in listdir(path) if not isfile(join(path, f))]

def get_files(path):
    return [join(path,f) for f in listdir(path) if isfile(join(path, f))]

sessions = []
for x in get_subdirs(data_path):
    sessions += get_subdirs(x)

blocks = []
for x in sessions:
    blocks += get_subdirs(x)

# Remove warmup blocks
blocks = [x for x in blocks if 'Warmup' not in x]

sentences = []
for x in blocks:
    sentences += get_files(x)

def count_chars(sentence):
    with open(sentence, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                correct = line
                count = 0
            elif i > 1:
                c = str(unichr(int(line.split()[1])))
                if c == correct[count]:
                    count += 1
                # We don't consider the rest of the phrase once we've found an error
                else:
                    if c < 2:
                        return 0
                    else:
                        return count + 1
        return count

def parse_sentence(sentence):
    with open(sentence, 'r') as f:
        typed_chars = []
        prev_time = None
        for i, line in enumerate(f.readlines()):
            if i == 0:
                correct_sentence = line
            elif i != 1:
                splits = line.split()
                time = int(splits[0])
                c = int(splits[1])
                for s in splits[2:]:
                    if s != '0':
                        print sentence
                        print splits

for sentence in sentences:
    parse_sentence(sentence)
