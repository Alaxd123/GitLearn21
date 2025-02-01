class Task:

    def __init__(self, title="Task", description=None, deadline=None):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.complete = False




class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self):
        for task in Task:
            self.tasks.append(Task)

    def delete_task(self):
        for task in self.tasks:
           self.delete_task(task_title)

    def mark_task_completed(self):
       self.complete = True

    def print_tasks(self):
        if self.tasks != []:
            print(f"Tasks Completed: {(self.task_title)}")
            for task in self.tasks:
                print(task)
            else:
                print("No tasks")



tasks_list = {
    "To do the dishes": {"deadline": 2},
    "To wash the car": {"deadline": 10},
    "To cook dinner": {"deadline": 1}
}



print(int(input("Write 1 to add tasks \n 2 to delete \n 3 to set tasks as complete \n 4 to rewatch tasks: ")))
if choice == 1:
    add_task(tasks_list) and print(input(""))




