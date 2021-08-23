    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class Payload(BaseModel):
    payload: Dict = {}