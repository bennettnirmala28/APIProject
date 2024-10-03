import json
import requests
import responses


#GET Request
def test_get_user():
    responses.add(responses.GET, "https://reqres.in/api/users/2",status=200)
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    json_data = response.json()
    json_str=json.dumps(json_data, indent=2)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")

#POST Request
def test_post_request():
    responses.add(responses.POST, "https://reqres.in/api/users", status=201)
    data = {"name": "morpheus","job": "leader"}
    response = requests.post("https://reqres.in/api/users" , json=data)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    print(".......POST/Create USER IS DONE.......")


#PUT Request
def test_put_request():
    responses.add(responses.PUT, "https://reqres.in/api/users/2",status=200)
    data={"name": "morpheus", "job": "zion resident"}
    response = requests.put("https://reqres.in/api/users/2", json=data)
    assert response.status_code == 200
    json_data = response.json()
    json_str=json.dumps(json_data, indent=2)
    assert json_data["job"] == "zion resident"
    print("json PUT response body: ", json_str)
    print(".......PUT/Update USER IS DONE.......")

# #DELETE Request
def test_delete_request():
    responses.add(responses.DELETE, "https://reqres.in/api/users/2",status=204)
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204
    print(".......DELETE USER IS DONE.......")


#call
test_get_user()
test_post_request()
test_put_request()
test_delete_request()
