from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title : Optional[str] = Field(None, example="간장 사기")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id : int

    class config:
        orm_mode = True

class Task(TaskBase):
    id : int
    done : bool = Field(False, description="완료 플래그")
    
    class Config :
        orm_mode = True