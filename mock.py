import requests
import responses


@responses.activate
def test_user():
    # Define the mock response for the GET request
    responses.add(
        responses.GET,
        "https://reqres.in/api/users/2",
        json={"error": "Access denied"},
        status=403
    )

    # Make the actual GET request
    response = requests.get("https://reqres.in/api/users/2")

    assert response.status_code == 403
    assert response.json()["error"] == "Access denied"

    print("Test passed: 403 Access denied")