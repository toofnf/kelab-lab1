from locust import HttpUser, task


class GetUser(HttpUser):
    @task
    def get_item_by_id(self):
        self.client.get("/items/1")
