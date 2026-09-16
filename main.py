import json
from datetime import datetime
class Task:
    def __init__(self, taskid, task, priority, category, description, due_date):
        self.taskid = taskid
        self.task = task
        self.priority = priority
        self.category = category
        self.description = description
        self.due_date = due_date

    def __str__(self):
        """
        returns in this format using print
        """
        return (
            f"ID: {self.taskid}\n"
            f"Task: {self.task}\n"
            f"Priority: {self.priority}\n"
            f"Category: {self.category}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}"
        )


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
        self.tasks.append(task)
        print("Task is added")

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
                return
        print("Task not found")

    def update_task(self, newtask):
        for i, task in enumerate(self.tasks):
            if task.taskid == newtask.taskid:
                self.tasks[i] = newtask
                return task

    def search_by_word(self, search_word):
        for task in self.tasks:
            if search_word.lower() in task.description.lower():
                # print(self.tasks[i])
                print(task)

    def filter_by_id(self, search_id):
        for task in self.tasks:
            if task.taskid == search_id:
                print(task)
                return
        print("Task not found")

    def filter_by_category(self, search_category):
        found = False

        # result=[]
        for task in self.tasks:
            if task.category.lower() == search_category.lower():
                print("-"*20)
                print(task)
                found = True
        if not found:

            print("Task not found")

def category_validation():
    while True:
        category = input("Enter category of task")
        if category.lower() in ['grocery', 'work', 'house', 'learning']:
            return category
        print("enter category from list: grocery, work, learning, house,")

def priority_validation():

    while True:
        priority = input("Enter priority of task")
        if priority.lower() in ['high', 'low','medium']:
            return priority
        print("please enter priority as low, medium and high")

def input_validation(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")

def duedate_validation():
    while True:
        due_date = input("Enter due date (yyyy-mm-dd) of the task ")
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

def taskid_validation():

    while True:
        task_id = input("enter task id: ")
        if task_id.isdigit():
            return task_id
        print("Enter task id as digit")


manager = Taskmanager()
manager.read_json()
while True:
    manager.show_menu()
    choice = input ("choose and option:")

    if choice == "1":
        task_id= taskid_validation()
        task = input_validation("Enter task to be added ")
        priority = priority_validation()
        category = category_validation()
        description = input_validation("enter description to task ")
        due_date = duedate_validation()

        todo_task= Task (
            task_id,
            task,
            priority,
            category,
            description,
            due_date)

        manager.add_task(todo_task)
        manager.save_json()

    elif choice == "2":
        # manager.read_json()
        manager.view_task()


    elif choice == "3":
        task_id = taskid_validation()
        task = input("Enter task to be added ")
        priority = priority_validation()
        category = category_validation()
        description = input("enter description to task ")
        due_date = duedate_validation()
        new_task = Task(
            task_id,
            task,
            priority,
            category,
            description,
            due_date)

        manager.update_task(new_task)
        manager.save_json()

    elif choice == "4":
        filter_id= input("enter id to be searched")
        manager.filter_by_id(filter_id)

    elif choice == "5":
        filter_category=input("enter category to be searched")
        manager.filter_by_category(filter_category)

    elif choice == "6":
        search_word=input("enter word to be searched")
        manager.search_by_word(search_word)

    elif choice == "7":
        remove_id= input("enter taskid to be removed")
        manager.remove_task(remove_id)
        manager.save_json()

    elif choice == "8":
        print("Thanks for using the To-Do App!")
        break

    else:
        print("Please choose a number from 1 to 7.")


