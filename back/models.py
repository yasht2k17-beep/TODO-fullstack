from sqlalchemy import Column,Integer,String,Boolean
from database import base

class ToDo(base):
    __tablename__="todo"

    id =Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    completed= Column(Boolean,default=False)

