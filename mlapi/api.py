from typing import Callable, Optional, Dict

from fastapi import FastAPI, UploadFile, File

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
        )

        docs_url = kwargs.get("docs_url", "/docs")
        title = kwargs.get("title", "MLAPI Model Server 🔥")

        self.app: FastAPI = FastAPI(title=title, description=desc, docs_url=docs_url)
        if not preprocess_conf:
            preprocess_conf = {}
        if not postprocess_conf:
            postprocess_conf = {}
        self.preprocess_conf = preprocess_conf
        self.postprocess_conf = postprocess_conf
        self.setup(**kwargs)
        
    async def predict(self, file: UploadFile = File(...)):
        preprocess_fn = self.data_processor.preprocess_fn
        postprocess_fn = self.data_processor.postprocess_fn

        x = preprocess_fn(await file.read())
        x = self.model(x)
        x = postprocess_fn(x)
        return x
