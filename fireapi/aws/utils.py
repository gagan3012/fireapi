            print('Current ID is %i' % uid)

        return uid  # return the user ID for use

    def get_valid_call_id(self, verbose=False):
        '''Get a function ID that has not been used for the current user yet'''
        fid = random.randint(self.lower_limit, self.upper_limit)  # propose a random integer as the new function ID
        valid = False
        while not valid:
            if fid in self.ids[self.curid]:  # if the current user has used it already
                fid = random.randint(self.lower_limit, self.upper_limit)  # propose a new one
            else:
                self.ids[self.curid].append(fid)  # otherwise add it to the list and use it and move on
                full_pickle(self.hd + '/current_session_ids', self.ids)  # save the id dictionary for todays session
                valid = True
        if verbose:
            print('Call ID is %i' % fid)

        return fid

    # Load the data needed for the module


username_dictionary = {'Linux': 'ec2-user',
                       'Ubuntu': 'ubuntu',
                       'Windows': 'ec2-user'}

spot_instance_pricing = pd.read_csv(pull_root() + '/data/spot_instance_pricing.csv')
ami_data = pd.read_csv(pull_root() + '/data/ami_data.csv')
ami_data['username'] = ami_data['image_name'].apply(lambda s: find_username(s))