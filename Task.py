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
