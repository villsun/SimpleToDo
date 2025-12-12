import tkinter as tk
from task_manager import TaskManager


class TodoApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("SimpleToDo")

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        tk.Button(root, text="Додати задачу", command=self.add_task).pack()
        tk.Button(root, text="Позначити виконану", command=self.mark_done).pack()
        tk.Button(root, text="Видалити задачу", command=self.delete_task).pack()

        self.listbox = tk.Listbox(root, width=40)
        self.listbox.pack(pady=10)

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for i, task in enumerate(self.manager.tasks, start=1):
            status = "✓" if task.is_done else " "
            self.listbox.insert(tk.END, f"{i}. [{status}] {task.text}")

    def add_task(self):
        text = self.entry.get().strip()
        if text:
            self.manager.add_task(text)
            self.entry.delete(0, tk.END)
            self.refresh()

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.manager.remove_task(index)
            self.refresh()

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.manager.mark_done(index)
            self.refresh()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
