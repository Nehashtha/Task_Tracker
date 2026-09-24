import json
from validation import category_validation,taskid_validation,priority_validation,input_validation,duedate_validation
from Task_manager import Taskmanager
from Task import Task


def main():
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


if __name__ == "__main__":
    main()