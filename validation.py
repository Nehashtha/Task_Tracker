from datetime import datetime

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
            return int(task_id)
        print("Enter task id as digit")
