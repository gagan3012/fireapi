from typing import Text, Union, List
from uuid import uuid4


def get_docker_file_contents(self, dockerfile_path: Text):
    if dockerfile_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        dockerfile_path = os.path.join(base_path, 'template.Dockerfile')

    with open(dockerfile_path, 'r') as f:
        docker_template_content = f.read()
        # TODO: Maybe use env variables for this
        docker_template_content = docker_template_content.replace(
            "$BASE_IMAGE", BUDGETML_BASE_IMAGE_NAME)
    return docker_template_content


def get_requirements_file_contents(self, requirements_path: Text):
    if requirements_path is None:
        requirements_content = ''
    else:
        with open(requirements_path, 'r') as f:
            requirements_content = f.read()
    return requirements_content


def get_docker_compose_contents(self, docker_compose_path: Text = None):
    if docker_compose_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        docker_compose_path = os.path.join(
            base_path, 'template-compose.yaml')

    with open(docker_compose_path, 'r') as f:
        docker_compose_content = f.read()
        return docker_compose_content


def get_nginx_conf_contents(self,
                            domain: Text,
                            subdomain: Text,
                            nginx_config_path: Text = None):
    if nginx_config_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))
        nginx_config_path = os.path.join(
            base_path, 'template-nginx.conf')

    with open(nginx_config_path, 'r') as f:
        nginx_config_content = f.read()
        nginx_config_content = nginx_config_content.replace(
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
    # create bucket if it doesnt exist
    if bucket_name is None:
        bucket_name = f'budget_bucket_{self.unique_id}'
    create_bucket_if_not_exists(bucket_name)