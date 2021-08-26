from typing import Callable, Optional, Dict

from fastapi import FastAPI

from mlapi.base import ModelServer


class API(ModelServer):
    def __init__(
        self,
        api_type: str,
        model: Callable,
        preprocess_fn: Optional[Callable] = None,
        preprocess_conf: Optional[Dict] = None,
        postprocess_fn: Optional[Callable] = None,
        postprocess_conf: Optional[Dict] = None,
        **kwargs,
    ):
