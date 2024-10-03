import requests
from tenacity import retry, stop_after_attempt,wait_exponential,retry_if_exception_type


class APIClient:
    def __init__(self,base_url):
        self.base_url=base_url

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1,min=2,max=10),retry=retry_if_exception_type((requests.exceptions.Timeout,requests.exceptions.ConnectionError)))
    def get(self ,endpoint):
        response=requests.get(f"{self.base_url}{endpoint}", timeout=5)
        response.raise_for_status()
        return response.json()

client=APIClient("https://reqres.in")
try:
    user_data=client.get("/api/users/2")
    print(user_data)
except requests.exception.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exception.RequestException as e:
    print(f"Request error occurred :{e}")