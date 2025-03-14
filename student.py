from pydantic import BaseModel


class Student(BaseModel):
    name: str
    is_active: bool = True
