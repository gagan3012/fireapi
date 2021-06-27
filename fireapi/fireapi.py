from typing import Text, Union, List
from uuid import uuid4


def launch_local(self,
                 predictor_class,
                 requirements: Union[Text, List] = None,
                 dockerfile_path: Text = None,
                 bucket_name: Text = None,
                 username: Text = 'budget',
                 password: Text = str(uuid4())):
    """
    Launch API locally at 0.0.0.0:8000 via docker to simulate endpoint
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
    if bucket_name is None:
        bucket_name = f'budget_bucket_{self.unique_id}'
    create_bucket_if_not_exists(bucket_name)