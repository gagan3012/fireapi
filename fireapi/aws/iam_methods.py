
        if 'InvalidGroup.Duplicate' in str(e):
            print('Security group detected, re-using...')
            sg = retrieve_security_group(spotid, client=client)
        else:
            raise e

    return sg