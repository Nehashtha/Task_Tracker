import json
from Task import Task

class Taskmanager():
    def __init__(self):
        self.tasks = []

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
        for task in self.tasks:
            print(task)
            print("-" * 20)

    def add_task(self, task):
        for existing_task in self.tasks:
            if existing_task.taskid==task.taskid:
                print("Task ID already exists")
                return False
        self.tasks.append(task)
        print("Task is added")
        return True

    def save_json(self):
        json_task_list=[]
        for task in self.tasks:
            json_task_list.append(task.__dict__)
        with open("json_task_list.json", "w") as file:
            json.dump(json_task_list, file, indent=4)
        print("data stored")


    def read_json(self):
        with open("json_task_list.json", "r", encoding="utf-8") as file:
            loaded_data = json.load(file)
        self.tasks=[]
        for task_data in loaded_data:
            task = Task(
                task_data["taskid"],
                task_data["task"],
                task_data["priority"],
                task_data["category"],
                task_data["description"],
                task_data["due_date"]
            )
            self.tasks.append(task)
        print("Tasks loaded sucessfully. ")
        # print(loaded_data)


    def remove_task(self, task_id):

        for i, task in enumerate(self.tasks):
            if task.taskid == task_id:
                self.tasks.pop(i)
                print("Task is removed")
                return True
        print("Task not found")
        return False

    def update_task(self, newtask):
        for i, task in enumerate(self.tasks):
            if task.taskid == newtask.taskid:
                self.tasks[i] = newtask
                print("Task updated")
                return True
        print("Task not found")
        return False

    def search_by_word(self, search_word):
        # results=[]
        for task in self.tasks:
            if search_word.lower() in task.description.lower():
                # results.append(task)
                # print(self.tasks[i])
                print(task)
        # return results
    def filter_by_id(self, search_id):
        for task in self.tasks:

            if task.taskid == int(search_id):
                print(task)
                return

    def filter_by_category(self, search_category):
        found = False

        for task in self.tasks:
            if task.category.lower() == search_category.lower():
                print("-" * 20)
                print(task)
                found = True
        if not found:
            print("Task not found")



