import sys, boto3
from fireapi.aws import utils


def create_key_pair(client, profile, kp_dir=None):
