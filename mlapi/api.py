from typing import Callable, Optional, Dict

from fastapi import FastAPI

from mlapi.base import ModelServer


class API(ModelServer):
    def __init__(
