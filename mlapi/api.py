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
        """
        Creates FastAPI app for `api_type`
        Args:
            model: Any ML/DL model
            preprocess_fn: Override Data Preprocessing Function, data will
            be processed with this function
            before calling model.
            postprocess_fn: Override Data Postprocessing Function, model
            output will be passed into this function.
            **kwargs:
        """
        super(API, self).__init__(
            api_type, model, preprocess_fn, postprocess_fn, **kwargs
