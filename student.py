from email.policy import default

from pydantic import BaseModel


class Student(BaseModel):
    id: int = default
    name: str
    email: str
    is_active: bool = True

