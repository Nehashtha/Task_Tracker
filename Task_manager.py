import json
from Task import Task
import sqlite3

class Taskmanager():
    def __init__(self, db_name='task_database.db'):
        self.tasks = []
        self.db_name=db_name

    def show_menu(self):
        print("1. Add task")
        print("2. View tasks")
        print("3. update task")
        print("4. Filter by taskid")
        print("5. Filter by category")
        print("6. search by word")
        print("7. Remove task")
        print("8. Exit")

    def view_task(self):
        db = sqlite3.connect('task_database.db')
        cur = db.cursor()
        sql="""SELECT * FROM task_tracker"""
        cur.execute(sql)
        result=cur.fetchall()
        return result
        db.close()

    def database(self):
        db=sqlite3.connect(self.db_name)
        cur=db.cursor()
        return db, cur
    def create_Database(self):
        db, cur = self.database()
        sql = """CREATE TABLE IF NOT EXISTS task_tracker(taskid INTEGER PRIMARY KEY, task TEXT NOT NULL, priority TEXT NOT NULL, category TEXT NOT NULL, description TEXT NOT NULL, duedate TEXT NOT NULL)"""
        cur.execute(sql)
        db.commit()
        db.close()

    def add_task(self, task):
        db,cur=self.database()
        sql="""INSERT INTO task_tracker(taskid,task,priority,category,description, duedate) values(?,?,?,?,?,?)"""
        cur.execute(sql,(task.taskid, task.task,task.priority, task.category, task.description, task.due_date))
        # self.tasks.append(task)
        db.commit()
        db.close()
        print("Task added to database")
        return True


    def remove_task(self, task_id):
        db, cur = self.database()
        sql ="""DELETE FROM task_tracker where taskid=?"""
        try:
            cur.execute(sql,(task_id,))
            db.commit()
            print("data deleted" )
            if cur.rowcount==0:
                return False
            return True
        finally:
            db.close()

    def update_task(self, newtask):
        db, cur = self.database()
        try:
            sql = """ UPDATE task_tracker 
                    SET task=?,priority=?, category=?, description=? 
                    where taskid=?"""
            taskid=newtask.taskid
            task=newtask.task
            priority=newtask.priority
            category=newtask.category
            description=newtask.description
            cur.execute(sql, (task,priority,category,description,taskid,))
            db.commit()
            return cur.rowcount > 0

        # print("Database is updated")
        finally:
            # db.commit()
            db.close()



    def search_by_word(self, search_word):
        """
        using try/ finally :make sure the database connection is always closed, even if an error occurs or the function returns early.
        :param search_word:
        :return:
        """
        db, cur = self.database()
        try:
            sql = """SELECT * FROM task_tracker WHERE description LIKE ?"""
            cur.execute(sql, ('%'+search_word+'%',))
            result=cur.fetchall()
            return result
        finally:

            db.close()


    def filter_by_id(self, search_id):

        db, cur = self.database()
        sql = """SELECT *FROM task_tracker where taskid=?"""
        cur.execute(sql,(search_id, ))
        result=cur.fetchone()
        db.close()
        return result

    def filter_by_category(self, search_category):
        db, cur = self.database()
        sql = """SELECT * FROM task_tracker where category=?"""
        cur.execute(sql, (search_category,))
        result=cur.fetchall()
        db.close()
        return result





