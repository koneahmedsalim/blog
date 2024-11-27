from locust import HttpUser, TaskSet, between, task

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def login(self):
        self.client.post("/login/", {"username": "test", "password": "password"})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
