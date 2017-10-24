class Task():
    is_done = False

    def __init__(self, name, description):
        self.name = name
        self. description = description

    def change_task_status(self):
        self.is_done = True

    def __str__(self):
        if is_done:
            return self.name + self.description + 'Done'
        else:
            return self.name + self.description + 'To Do'
