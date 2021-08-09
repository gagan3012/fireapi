import sys, boto3
from fireapi.aws import utils


def create_key_pair(client, profile, kp_dir=None):
    # Create a key pair on AWS
    keypair = client.create_key_pair(KeyName=profile['key_pair'][0])

    if kp_dir is None:
        kp_dir = utils.get_default_kp_dir()

    # Download the private key into the CW
    with open(kp_dir + '/' + profile['key_pair'][1], 'w') as file:
        file.write(keypair['KeyMaterial'])
        file.close()
    print('Key pair ' + profile['key_pair'][0] + ' created...')


def retrieve_security_group(spotid, client=None, region=None):
    if client is None:
        assert region is not None
        client = boto3.client('ec2', region_name=region)

    elif region is None:
        assert client is not None

    sg = client.describe_security_groups(Filters=[{'Name': 'group-name', 'Values': [spotid]}])['SecurityGroups'][0]
