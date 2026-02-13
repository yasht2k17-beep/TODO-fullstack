from pydantic import BaseModel
class CreateTask(BaseModel):
    title:str

class ResponseTask(BaseModel):
    id:int
    title:str
    completed:bool

class Config:
    from_attributes=True