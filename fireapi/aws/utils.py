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
    '''Load the profiles from the package profile.txt file'''

    profile = \
    [f for f in list(absoluteFilePaths(os.path.join(pull_root(), 'data'))) if os.path.split(f)[-1] == 'profiles.txt'][0]

    with open(profile, 'r') as f:
        profiles = ast.literal_eval(f.read())

    # print('Profiles loaded, you can edit profiles in '+str(profile))

    return profiles


def save_profiles(profiles):
    '''Save the profile dict str in a .txt file'''
    profile_file = \
    [f for f in list(absoluteFilePaths(os.path.join(pull_root(), 'data'))) if os.path.split(f)[-1] == 'profiles.txt'][0]

    # ptosave = ast.literal_eval(profile_str)
    print(profile_file)

    with open(profile_file, 'w') as f:
        f.write(pprint.pformat(profiles))
        f.close()


def default_region():
    profiles = load_profiles()
    print(profiles['default']['region'])


def change_default_region(region, deactive_warning=True):
    if not deactive_warning:
        ans = input('Warning: doing this will change the "region" for all profiles. Continue?(y): ')
        if ans != 'y':
            raise Exception('User exit')

    profiles = load_profiles()
    for k in profiles:
        profiles[k]['region'] = region

    save_profiles(profiles)


def change_default_image(image, deactive_warning=True):
    if not deactive_warning:
        ans = input('Warning: doing this will change the "image_id" for all profiles. Continue?(y): ')
        if ans != 'y':
            raise Exception('User exit')

    profiles = load_profiles()
    for k in profiles:
        profiles[k]['image_id'] = image

