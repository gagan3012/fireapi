import os, ast, boto3, random, string, pprint, glob, re, psutil
import _pickle as pickle
import pandas as pd
import numpy as np
from path import Path
from IPython.display import clear_output
from datetime import datetime

root = Path(os.path.dirname(os.path.abspath(__file__)))


def full_pickle(title, data):
    '''pickles the submited data and titles it'''
    pikd = open(title + '.pickle', 'wb')
    pickle.dump(data, pikd)
    pikd.close()


def loosen(file):
    '''loads and returns a pickled objects'''
    pikd = open(file, 'rb')
    data = pickle.load(pikd)
    pikd.close()
    return data


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def genrs(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def absoluteFilePaths(directory):
    '''Get the absolute file path for every file in the given directory'''

    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


def pull_root():
    '''Retrieve the directory for this instance'''
    return Path(os.path.dirname(os.path.abspath(__file__)))


def load_profiles():
