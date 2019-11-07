from pydantic import BaseModel


class Int(BaseModel):
    result: int
    time: str
