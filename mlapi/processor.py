from typing import Callable, Optional


class DataProcessor:
    def __init__(
        self,
        preprocess_fn: Optional[Callable] = None,
