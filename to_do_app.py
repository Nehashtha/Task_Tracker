def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Change status")
    print("4. Filter by taskid")
    print("5. Filter by category")
    print("6. search by word")
    print("7. Remove task")
    print("8. Exit")


def add_task(todo_task):
    """
    :param todo_task: Empty dictionary where task information is added
    """
    task = input("enter task to be added ")
    priority = input("Enter priority (high/medium/low):")
    category = input("enter category to task (Work, House, Grocery, Learning) ")
    description = input("enter description to task ")
    due_date = input("enter due date to task (yyyy-mm-dd) ")

    task_id = len(todo_task) + 1

    todo_task[task_id] = {
        "task": task,
        "priority": priority,
        "status": False,
        "category": category,
        "description": description,
        "due_date": due_date

    }
    print("Task added!")


def view_task(todo_task):
    if not todo_task:
        print("Dictionary is empty")
        return
    print(f"{'ID':<5} | {'Task':<10} | {'Priority':<10}| {'Category':<10}| {'Description':<30}| {'Due date':<10}")
    print("-" * 100)
    for task_id, task in todo_task.items():

        print(f"{task_id:<5}| {task['task']:<10} | {task['priority']:<10} | {task['category']:<10} |{task['description']:<20} |{task['due_date']:<10} ")


def change_status(todo_task):
    task_update = input("Enter task id to be marked")
    for task_id, task in todo_task.items():
        if task_id == int(task_update):
            if not task["status"]:
                task["status"] = True


def filter_by_taskid(todo_task):
    search_task_id = input("Enter task id to search  task")
    for task_id, task in todo_task.items():
        if task_id == int(search_task_id):
            print(f"{task_id:<5}| {task['task']:<10} | {task['priority']:<10} | {task['category']:<10} |{task['description']:<20} |{task['due_date']:<10} ")


def filter_by_category(todo_task):
    search_category_input= input("Enter category to search task")
    search_category = search_category_input.lower()
    for task_id, task in todo_task.items():
        if task['category'] == search_category:
            print(f"{task_id:<5}| {task['task']:<10} | {task['priority']:<10} | {task['category']:<10} |{task['description']:<20} |{task['due_date']:<10} ")


def search( todo_task):
    search_word = input("Enter word to search task").lower()
    for task_id, task in todo_task.items():
        if search_word in task['description']:
            print(f"{task_id:<5}| {task['task']:<10} | {task['priority']:<10} | {task['category']:<10} |{task['description']:<20} |{task['due_date']:<10} ")


def remove_task( todo_task):
    task_remove_id = input("Enter task id to be remove")
    for task_id, task in todo_task.items():
        if task_id == int(task_remove_id):
            todo_task.pop(task_id)
            print(f"Removed task: {task_id}")
            break

def main():
    """
    Steps
    1. show menu
    2. User chooses option from menu
    3. choice 1, user adds task information
    4. choice 2, view list of task
    5. choice 3, change status
    6. choice 4, filter by task id
    7. choice 5, filter by category
    8. choice 6, search by word
    9. choice 7, remove task
    10. choice 8, exit

    :return:
    """
    todo_task = {}
    #while true keeps on repeating until user defines exit

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(todo_task)

        elif choice == "2":
           view_task(todo_task)

        elif choice == "3":
            change_status(todo_task)

        elif choice == "4":
            # search_taskid(todo_task)
            filter_by_taskid(todo_task)

        elif choice == "5":
            filter_by_category(todo_task)

        elif choice == "6":
            search(todo_task)

        elif choice == "7":
            remove_task(todo_task)

        elif choice == "8":
            print("Thanks for using the To-Do App!")
            break

        else:
            print("Please choose a number from 1 to 7.")


main()

