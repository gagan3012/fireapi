
username_dictionary = {'Linux': 'ec2-user',
                       'Ubuntu': 'ubuntu',
                       'Windows': 'ec2-user'}

spot_instance_pricing = pd.read_csv(pull_root() + '/data/spot_instance_pricing.csv')
ami_data = pd.read_csv(pull_root() + '/data/ami_data.csv')
ami_data['username'] = ami_data['image_name'].apply(lambda s: find_username(s))