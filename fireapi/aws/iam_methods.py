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
    return sg


# TODO : Split security group functions into create and retrieve

def get_security_group(client, spotid: str, enable_nfs: bool = False, enable_ds: bool = False,
                       firewall_ingress_settings=None):

    if firewall_ingress_settings is not None:
        assert type(firewall_ingress_settings) == tuple
        assert len(firewall_ingress_settings) == 4

    try:
        # Create a security group for the current spot instance id
        sg = client.create_security_group(GroupName=spotid,
                                          Description='SG for ' + spotid)

        if enable_nfs:
            # Add NFS rules (port 2049) in order to connect an EFS instance
            client.authorize_security_group_ingress(GroupName=spotid,
                                                    IpPermissions=[
                                                        {'FromPort': 2049,
                                                         'IpProtocol': 'tcp',
                                                         'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                                                         'ToPort': 2049,
                                                         }
                                                    ])

        if enable_ds:
            # Add ingress & egress rules to enable datasync
            # Add HTTP and HTTPS rules (port 80 & 443) in order to connect to datasync agent
            client.authorize_security_group_ingress(GroupName=spotid,
                                                    IpPermissions=[
                                                        {'FromPort': 80,
                                                         'IpProtocol': 'tcp',
