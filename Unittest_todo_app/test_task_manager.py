import unittest
from task import Task
from task_manager import TaskManager

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Buy milk")
        self.assertEqual(task.text, "Buy milk")
        self.assertFalse(task.is_done)

    def test_mark_done(self):
        task = Task("Read book")
        task.mark_done()
        self.assertTrue(task.is_done)


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Buy milk")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].text, "Buy milk")

    def test_remove_task(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.manager.remove_task(0)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].text, "Task 2")

    def test_mark_done_task(self):
        self.manager.add_task("Task 1")
        self.manager.mark_done(0)
        self.assertTrue(self.manager.tasks[0].is_done)

    def test_remove_invalid_index(self):
        self.manager.add_task("Task 1")
        self.manager.remove_task(5)
        self.assertEqual(len(self.manager.tasks), 1)

    def test_mark_done_invalid_index(self):
        self.manager.add_task("Task 1")
        self.manager.mark_done(5)
        self.assertFalse(self.manager.tasks[0].is_done)


if __name__ == "__main__":
    unittest.main()
