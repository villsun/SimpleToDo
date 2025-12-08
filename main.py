from task_manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\n1 — Додати задачу")
        print("2 — Показати задачі")
        print("3 — Відмітити виконану")
        print("4 — Видалити задачу")
        print("0 — Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            text = input("Введіть текст задачі: ")
            manager.add_task(text)

        elif choice == "2":
            for i, task in enumerate(manager.tasks, start=1):
                status = "✅" if task.is_done else "❌"
                print(f"{i}. {task.text} {status}")

        elif choice == "3":
            index = int(input("Номер задачі: ")) - 1
            manager.mark_done(index)

        elif choice == "4":
            index = int(input("Номер задачі: ")) - 1
            manager.remove_task(index)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()
