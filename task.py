class Task:
    def __init__(self, text: str):
        self.text = text
        self.is_done = False

    def mark_done(self):
        self.is_done = True