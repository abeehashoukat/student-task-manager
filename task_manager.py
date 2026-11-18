class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = {"id": self._next_id, "title": title, "completed": False}
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        return list(self.tasks)

    def _find(self, task_id):
     for t in self.tasks:
        if t["id"] == task_id:
            return t
     raise KeyError(f"No task with id {task_id}")
    
    # --- complete (implemented in feature/complete-task) ---
    def complete_task(self, task_id):
     task = self._find(task_id)
     task["completed"] = True
     return task

    # --- delete (implemented in feature/delete-task) ---
    def delete_task(self, task_id):
        raise NotImplementedError