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

