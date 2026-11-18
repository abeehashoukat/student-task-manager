import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.m = TaskManager()

    def test_add_task(self):
        t = self.m.add_task("Study Git")
        self.assertEqual(t["title"], "Study Git")
        self.assertEqual(len(self.m.list_tasks()), ... , 2)

    def test_add_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            self.m.add_task("   ")

    def test_complete_task(self):
        t = self.m.add_task("Finish lab")
        self.m.complete_task(t["id"])
        self.assertTrue(self.m.list_tasks()[0]["completed"])

    def test_delete_task(self):
        t = self.m.add_task("Temp")
        self.m.delete_task(t["id"])
        self.assertEqual(self.m.list_tasks(), [])

    def test_delete_invalid_id(self):
        with self.assertRaises(KeyError):
            self.m.delete_task(999)


if __name__ == "__main__":
    unittest.main()