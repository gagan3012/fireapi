from typing import Dict, Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Optional[str] = None
