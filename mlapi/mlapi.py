from pydantic import BaseModel

from fastapi import Depends, FastAPI, File, UploadFile, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
