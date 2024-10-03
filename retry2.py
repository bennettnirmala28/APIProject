import responses
from locust import HttpUser, task, between

class Reqres(HttpUser):
    wait_time=between(1,2)
    host = "https://reqres.in"

    @task
    def get_user(self):
        response=self.client.get("/api/users/2")
        if response.status_code==200:
            print(f"USer Retrieved: {response.json()['data']['first_name']}")
        else:
            print("Failed to retrieve user")
@responses.activate
def mock_server_error():
    responses.add(responses.GET,"https://reqres.in/api/users/2", status=500)

    responses.add(responses.GET,"https://reqres.in/api/users/2", json={"data":{"id":2,"first_name":"Janet"}}, status=200)


mock_server_error()
