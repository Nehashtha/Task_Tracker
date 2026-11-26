from fastapi import FastAPI, HTTPException, status
import sqlite3
from api_module import taskCreate


app = FastAPI(
    title="Task Tracker API",
    description="API for managing tasks using FastAPI and SQLite",
    version="1.0.0"
)

@app.get("/")
async def home():
    return {"Welcome to task tracker!"}
def db_connect():
    """
    db.row_factory = sqlite3.Row allows you to convert rows into dictionaries using dict(row).
    :return:
    """
    db = sqlite3.connect('task_database.db')
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    return db,cur

@app.get("/tasks",status_code=status.HTTP_200_OK)

def get_all_tasks():
    db,cur=db_connect()
    sql="""SELECT * FROM task_tracker"""
    cur.execute(sql)
    rows=cur.fetchall()

    tasks = [dict(row) for row in rows]

    db.close()
    return tasks

@app.post("/add/tasks", status_code=status.HTTP_201_CREATED)
def add_task(new_task:taskCreate):
    db,cur=db_connect()
    sql="""INSERT INTO task_tracker (task, priority, category, description, duedate)
        VALUES (?, ?, ?, ?, ?)"""
    cur.execute(sql,(new_task.task,new_task.priority,new_task.category, new_task.description,new_task.duedate,))
    db.commit()
    task_id = cur.lastrowid

    cur.execute(
        "SELECT * FROM task_tracker WHERE taskid = ?",
        (task_id,)
    )

    new_task_data = dict(cur.fetchone())

    db.close()

    return new_task_data

@app.put("/update/tasks/{taskid}")
def update_task(new_task:taskCreate,taskid:int):
    db,cur=db_connect()

    sql= """ UPDATE task_tracker 
                    SET task=?,priority=?, category=?, description=? ,duedate=?
                    where taskid=?"""

    cur.execute(sql,(new_task.task,new_task.priority,new_task.category, new_task.description,new_task.duedate, taskid))
    db.commit()
    updated=cur.rowcount
    if updated==0:

        db.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    cur.execute("SELECT * FROM task_tracker WHERE taskid=?", (taskid,))
    updated_task = dict(cur.fetchone())

    db.close()

    return updated_task


@app.get("/tasks/{taskid}")
def filter_by_id(taskid: int):
    db,cur=db_connect()
    sql="""SELECT * FROM task_tracker WHERE taskid = ?"""
    cur.execute(sql, (taskid,))
    row=cur.fetchone()

    db.close()
    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found")

    return dict(row)
    # return tasks


@app.get("/tasks/search/{search_word}")
def search_by_word(search_word:str):
    db,cur=db_connect()
    cur.execute('SELECT * FROM task_tracker WHERE description LIKE ? ',('%'+search_word+'%',))
    result=cur.fetchall()
    db.close()
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return [dict(row) for row in result]
#

@app.get("/tasks/category/{category}")
def filter_by_category(category: str):
    db,cur=db_connect()
    cur.execute("SELECT * FROM task_tracker WHERE category=?", (category,))
    result=cur.fetchall()
    db.close()
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return [dict(row) for row in result]
    # return result

@app.delete("/delete/tasks/{taskid}",status_code=status.HTTP_204_NO_CONTENT)
def remove_task(taskid: int):
    db,cur=db_connect()
    result=cur.execute("DELETE FROM task_tracker WHERE taskid=?",(taskid,))
    db.commit()
    deleted=cur.rowcount
    db.close()
    if deleted==0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return




