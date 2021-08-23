import itertools
from typing import Callable, Optional, List


class ModelServer:
    API_TYPES = {}

    def __init__(
        self,
        api_type: str,
        model: Callable,
        preprocess_fn=None,
        postprocess_fn=None,
        preprocess_conf: Optional[dict] = None,
