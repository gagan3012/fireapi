import sys, boto3
from fireapi.aws import utils


def create_key_pair(client, profile, kp_dir=None):
    # Create a key pair on AWS
    keypair = client.create_key_pair(KeyName=profile['key_pair'][0])

