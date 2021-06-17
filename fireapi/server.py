import logging
import os
import traceback
from typing import Optional, Any, Type

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
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def verify(token: str = Depends(oauth2_scheme)):
    try:
        if token == os.getenv('TOKEN'):
            return token
        raise Exception
    except Exception as e:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials with error {}".format(
                str(e)),
            headers={"WWW-Authenticate": "Bearer"},
        )

PREDICTOR: Optional[Any] = None

@app.on_event("startup")
async def startup_event():
    global PREDICTOR
    global USERS_DB

    # Setting auth creds
    USERS_DB = {
        'username': os.environ['BUDGET_USERNAME'],
        'password': os.environ['BUDGET_PWD'],
    }

    try:
        PREDICTOR_CLASS_PATH = os.getenv('BUDGET_PREDICTOR_PATH')
        assert PREDICTOR_CLASS_PATH is not None

        ENV_PREDICTOR_ENTRYPOINT = os.getenv('BUDGET_PREDICTOR_ENTRYPOINT',
                                             'Predictor')
        # Load predictor
        PREDICTOR.load()
    except Exception as e:
        logging.debug(f"Predictor class could not be loaded with: {str(e)}")
        traceback.print_exc()

@app.get("/")
def health_check():
    return {"message": "Welcome to Fire ML Please visit docs to get started"}
