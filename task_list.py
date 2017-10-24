from task import Task


class TaskList():
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        todo_task = Task(name, description)
        self.tasks.append(todo_task)

    def modify_task(self, name, description, index):
        todo_task = Task(name, description)
        self.tasks.insert(index, todo_task)

    def remove_task(self, index):
        self.tasks.pop(index)

    def __str__(self):
        task_number = 1
        task_string = ''
        for item in self.tasks:
            item = str(task_number) + ' ' + str(item)
            task_string += item + '\n'
            task_number += 1
        return task_string
