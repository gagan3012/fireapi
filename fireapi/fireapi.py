from typing import Text, Union, List
from uuid import uuid4


def launch_local(self,
                 predictor_class,
                 requirements: Union[Text, List] = None,
                 dockerfile_path: Text = None,
