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
