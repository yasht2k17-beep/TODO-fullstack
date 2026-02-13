from fastapi import FastAPI,Depends,HTTPException
from database import engine,base,sessionLocal
from sqlalchemy.orm import Session
import models
import schemas

app= FastAPI()

base.metadata.create_all(bind=engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todo",response_model=schemas.ResponseTask)

def create_task(task:schemas.CreateTask, db:Session=Depends(get_db)):
    new_task=models.ToDo(title=task.title,completed=False)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/todo",response_model=list[schemas.ResponseTask])

def get_tasks(db:Session=Depends(get_db)):
    tasks=db.query(models.ToDo).all()
    return tasks

@app.delete("/todo/{task_id}")

def delete_task(task_id: int, db:Session=Depends(get_db)):
    task=db.query(models.ToDo).filter(models.ToDo.id==task_id).first()

    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"message":"Task deleted successfully"}

@app.put("/todo/{task_id}",response_model=schemas.ResponseTask)

def mark_done(task_id:int,db:Session=Depends(get_db)):
    task=db.query(models.ToDo).filter(models.ToDo.id==task_id).first()
    
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    
    task.completed=True
    db.commit()
    db.refresh(task)

    return task