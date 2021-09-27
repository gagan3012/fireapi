import itertools
from typing import Callable, Optional, List


class ModelServer:
    API_TYPES = {}

    def __init__(
        self,
        api_type: str,
        model: Callable,
        preprocess_conf: Optional[dict] = None,
        postprocess_conf: Optional[dict] = None,
        **kwargs,
    ):
        if not preprocess_conf:
            preprocess_conf = {}
        if not postprocess_conf:
            postprocess_conf = {}

        self.api_type = api_type.upper()
        self.model = model
        self.preprocess_conf = preprocess_conf
        self.postprocess_conf = postprocess_conf


    @classmethod
    def get_available_api_types(cls) -> List[str]:
        return list(itertools.chain.from_iterable(cls.API_TYPES.values()))