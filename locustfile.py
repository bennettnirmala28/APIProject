from locust import HttpUser, task, between


class ReqresUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://reqres.in"  # Set the host here # Simulate users waiting between 1 to 3 seconds between tasks

    @task
    def get_user(self):
        # Simulates a GET request to retrieve a user's details
        response = self.client.get("/api/users/2")
        if response.status_code == 200:
            print(f"Successfully retrieved user: {response.json()['data']['first_name']}")
        else:
            print(f"Failed to retrieve user: {response.status_code}")

    @task
    def create_user(self):
        # Simulates a POST request to create a new user
        response = self.client.post("/api/users", json={"name": "morpheus", "job": "leader"})
        if response.status_code == 201:
            print(f"Successfully created user: {response.json()['name']}")
        else:
            print(f"Failed to create user: {response.status_code}")

    @task
    def update_user(self):
        # Simulates a PUT request to update a user's details
        response = self.client.put("/api/users/2", json={"name": "morpheus", "job": "zion resident"})
        if response.status_code == 200:
            print(f"Successfully updated user: {response.json()['name']}")
        else:
            print(f"Failed to update user: {response.status_code}")

    @task
    def delete_user(self):
        # Simulates a DELETE request to delete a user
        response = self.client.delete("/api/users/2")
        if response.status_code == 204:
            print("Successfully deleted user.")
        else:
            print(f"Failed to delete user: {response.status_code}")
