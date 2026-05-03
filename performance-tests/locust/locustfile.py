from locust import HttpUser, task, between
import random


class TaskUser(HttpUser):
    wait_time = between(1, 3)
    task_ids = []

    def on_start(self):
        response = self.client.get("/tasks")

        if response.status_code == 200:
            tasks = response.json()
            self.task_ids = [task["id"] for task in tasks]

    @task(5)
    def get_tasks(self):
        self.client.get("/tasks")

    @task(2)
    def get_task_by_id(self):
        if not self.task_ids:
            return

        task_id = random.choice(self.task_ids)
        self.client.get(f"/tasks/{task_id}")

    @task(2)
    def create_task(self):
        response = self.client.post(
            "/tasks",
            json={
                "title": f"Load test task {random.randint(1, 100000)}",
                "description": "Created during performance test"
            }
        )

        if response.status_code == 200:
            task_id = response.json()["id"]
            self.task_ids.append(task_id)

    @task(1)
    def update_task(self):
        if not self.task_ids:
            return

        task_id = random.choice(self.task_ids)

        response = self.client.put(
            f"/tasks/{task_id}",
            json={
                "title": f"Updated task {random.randint(1, 100000)}",
                "completed": random.choice([True, False])
            }
        )

        if response.status_code == 404:
            self.task_ids.remove(task_id)

    @task(1)
    def delete_task(self):
        if not self.task_ids:
            return

        task_id = random.choice(self.task_ids)

        response = self.client.delete(f"/tasks/{task_id}")

        if response.status_code == 200:
            self.task_ids.remove(task_id)