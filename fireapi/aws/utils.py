def split_workloads(n_jobs, workload, wrkdir=None, filename=None):
    '''Split the workload into n_jobs which are saved as pickle files in the wrkdir under the filename<i> for each job i
    This is meant to be used to create the upload material for distributed jobs.
    __________
    parameters
    - n_jobs : int. number of files to split the workload into
    - workload : list. The items that will be split and pickled
    - wrkdir : str. The path to store the files for each job. If no directory is submitted the working directory will be printed.
    - filename : str. The prefix of each job file, the default title is "current_workload"
    '''

    if wrkdir is None:
        wrkdir = os.path.join(pull_root(), 'data')
        if not os.path.exists(wrkdir):
            try:
                os.mkdir(wrkdir)
            except Exception as e:
                print(
                    'Failed to make directory, submiting an existing directory will fix this. Otherwise you can change permissions.')
                raise e

    assert os.path.exists(wrkdir)

    if filename is None:
        filename = wrkdir + '/current_workload'
    else:
        filename = wrkdir + '/' + filename

    workload_size = int(np.ceil(len(workload)) / n_jobs)

    workload_list = [c for c in chunks(workload, workload_size)]

    wnum = 0
    filenames = []
    for work in workload_list:
        full_pickle(filename + '_' + str(wnum), work)
        filenames.append(filename + '_' + str(wnum) + '.pickle')
        wnum += 1

    return filenames


class CurrentIdLog:

    def __init__(self, logdir=None, lower_limit=0, upper_limit=9999999):
        '''
        A log class to keep track of the user and call Ids that have been used today.
        This class was designed to avoid using repeat user id numbers and call numbers which will return an error in the API.
        We reset by day because call numbers are reset in the API system after a short ammount of time.
        __________
        parameters
        - logdir : str. the directory to load or store the "current_session_ids.pickle" file which contains the IDs that have been used today so far.
        '''
        self.curid = None
        self.ids = None
        self.hd = None

        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

        date = datetime.today().date()

        if logdir is None:
            self.hd = os.path.join(pull_root(), 'data')
        else:
            self.hd = logdir

        if os.path.exists(self.hd + '/current_session_ids.pickle'):
            self.ids = loosen(self.hd + '/current_session_ids.pickle')  # load any existing log
            if self.ids['date'] != date:  # if it is from a different date we reset it
                self.ids = {}
                self.ids['date'] = date  # and set its date to today
        else:
            self.ids = {}
            self.ids['date'] = date

    def add_user_id(self, uid):
        '''Add a user ID to the list of unavailable IDs'''
        self.ids[uid] = []

    def set_user_id(self, uid):
        '''Set the current session ID'''
        self.curid = uid
        if uid not in self.ids:
            self.add_user_id(uid)

    def add_call_id(self, fid):
        '''Log that the current fid has been used with the current session id'''
        self.ids[self.curid].append(fid)

    def get_valid_user_id(self, verbose=False):
        '''Get a user ID that has not been used yet'''
        uid = random.randint(self.lower_limit, self.upper_limit)  # propose a random integer as the new user ID
        valid = False
        while not valid:
            if uid in self.ids:  # if it is in the current list of used IDs
                uid = random.randint(self.lower_limit, self.upper_limit)  # propose another
            else:
                self.set_user_id(uid)  # otherwise set it as the current ID and move on
                full_pickle(self.hd + '/current_session_ids', self.ids)  # save the id dictionary for todays session
                valid = True
        if verbose:
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