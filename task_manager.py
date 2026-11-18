class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
     title = (title or "").strip()
     if not title:
        raise ValueError("Task title cannot be empty")
     task = {"id": self._next_id, "title": title, "completed": False}
     self.tasks.append(task)
     self._next_id += 1
     return task

    def list_tasks(self):
        return list(self.tasks)

    # --- complete (implemented in feature/complete-task) ---
    def complete_task(self, task_id):
        raise NotImplementedError

    # --- delete (implemented in feature/delete-task) ---
    def delete_task(self, task_id):
        raise NotImplementedError