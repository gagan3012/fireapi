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
                                                         'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                                                         'ToPort': 80,
                                                         },
                                                        {'FromPort': 443,
                                                         'IpProtocol': 'tcp',
                                                         'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                                                         'ToPort': 443,
                                                         }
                                                    ])

            # Add HTTPS egress rules (port 443) in order to connect datasync agent instance to AWS
            client.authorize_security_group_egress(GroupId=sg['GroupId'],
                                                   IpPermissions=[
                                                       {'FromPort': 443,
                                                        'IpProtocol': 'tcp',
                                                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                                                        'ToPort': 443,
                                                        }
                                                   ])

            # Define ingress rules OTHERWISE YOU WILL NOT BE ABLE TO CONNECT
        if firewall_ingress_settings is not None:
            client.authorize_security_group_ingress(GroupName=spotid,
                                                    IpPermissions=[
                                                        {'FromPort': firewall_ingress_settings[1],
                                                         'IpProtocol': firewall_ingress_settings[0],
                                                         'IpRanges': [
                                                             {'CidrIp': firewall_ingress_settings[3],
                                                              'Description': 'ips'
                                                              },
                                                         ],
                                                         'ToPort': firewall_ingress_settings[2],
                                                         }
                                                    ])

        sys.stdout.write("Security Group " + spotid + " Created...")
        sys.stdout.flush()

    except Exception as e:

        if 'InvalidGroup.Duplicate' in str(e):
            print('Security group detected, re-using...')
            sg = retrieve_security_group(spotid, client=client)
        else:
            raise e

    return sg