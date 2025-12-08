from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, text: str):
        task = Task(text)
        self.tasks.append(task)

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_done(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
