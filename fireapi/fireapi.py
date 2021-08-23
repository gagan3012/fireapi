    before a proper launch.
    :param predictor_class: class of type budgetml.BasePredictor
    :param username: username for FastAPI endpoints
    :param password: password for FastAPI endpoints
    :param dockerfile_path: path to dockerfile
    :param requirements: Path to requirements or a list of python
    requirements. Use one of `dockerfile_path` or `requirements`
    :param bucket_name: name of bucket to store predictor class.
    :return:
    """
    # create bucket if it doesnt exist
    if bucket_name is None:
        bucket_name = f'budget_bucket_{self.unique_id}'
    create_bucket_if_not_exists(bucket_name)