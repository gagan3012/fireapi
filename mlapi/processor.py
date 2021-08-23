from typing import Callable, Optional


class DataProcessor:
    def __init__(
        self,
        preprocess_fn: Optional[Callable] = None,
        postprocess_fn: Optional[Callable] = None,
    ):
        self._preprocess_fn = preprocess_fn
        self._postprocess_fn = postprocess_fn
