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