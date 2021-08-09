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

    save_profiles(profiles)


def show_instances():
    client = boto3.client('ec2', region_name='us-west-2')
    print('Instances (by Key names):')
    for i in [res['Instances'][0] for res in client.describe_instances()['Reservations']]:
        print('     - "' + i['KeyName'].split('-')[1] + '" Type: ' + i['InstanceType'] + ', ID: ' + i['InstanceId'],
              flush=True)


def list_instance_profiles():
    '''List all instance profile roles avaialable. Instance profiles assign roles to instances so they can access other AWS services like S3.'''
    iam_client = boto3.client('iam')
    return iam_client.list_instance_profiles()


def printTotals(transferred, toBeTransferred):
    '''Print paramiko upload transfer'''
    print("Transferred: %.3f" % float(float(transferred) / float(toBeTransferred)), end="\r", flush=True)


def get_package_kp_dir():
    '''Get the key-pair directory'''
    kpfile = [f for f in list(absoluteFilePaths(os.path.join(pull_root(), 'data'))) if
              os.path.split(f)[-1] == 'key_pair_default_dir.txt'][0]
    with open(kpfile, 'r') as f:
        default_path = f.read()
        f.close()
    return default_path


def get_default_kp_dir():
    '''Get the default key pair directory'''
    kp_dir = get_package_kp_dir()
    return kp_dir


def set_default_kp_dir(directory: str):
    '''Set the default key pair directory'''
    kpfile = [f for f in list(absoluteFilePaths(os.path.join(pull_root(), 'data'))) if
              os.path.split(f)[-1] == 'key_pair_default_dir.txt'][0]
    with open(kpfile, 'w') as f:
        f.write(directory)
        f.close()
    print('Default path has been set to ' + kpfile)


def clear_key_pairs():
    '''Erase all the key pairs in the kp_directory'''
    answer = input(
        'You are about to erase all the locally stored key pairs.\nYou will have to erase the matching key board through the AWS dashboard. Conitnue? (Y)')

    if answer == 'Y':
        for f in glob.glob(get_default_kp_dir() + '/*'):
            os.remove(f)
    else:
        raise Exception('User exit')


def find_username(s):
    for k in username_dictionary:
        ios = re.findall('(' + k + ')', s)
        if len(ios) > 0:
            ios = username_dictionary[ios[0]]
            break
    return ios

