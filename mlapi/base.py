import itertools
from typing import Callable, Optional, List


class ModelServer:
    API_TYPES = {}

    def __init__(
        self,
        api_type: str,
