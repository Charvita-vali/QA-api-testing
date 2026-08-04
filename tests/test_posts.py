import requests

from config import BASE_URL, REQUEST_TIMEOUT


def test_get_single_post():
    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 200, (
        f"Expected status code 200, but received "
        f"{response.status_code}: {response.text}"
    )

    assert "application/json" in response.headers.get("Content-Type", ""), (
        "Expected a JSON response."
    )

    assert response.elapsed.total_seconds() < 5, (
        f"Response took too long: {response.elapsed.total_seconds()} seconds."
    )

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert isinstance(data["userId"], int)


def test_get_post_not_found():
    response = requests.get(
        f"{BASE_URL}/posts/9999",
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 404, (
        f"Expected status code 404, but received "
        f"{response.status_code}: {response.text}"
    )


def test_create_post():
    payload = {
        "title": "QA Testing Post",
        "body": "This is a test post created via automated API testing.",
        "userId": 1,
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 201, (
        f"Expected status code 201, but received "
        f"{response.status_code}: {response.text}"
    )

    assert "application/json" in response.headers.get("Content-Type", "")

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
    assert isinstance(data["id"], int)


def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body content.",
        "userId": 1,
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 200, (
        f"Expected status code 200, but received "
        f"{response.status_code}: {response.text}"
    )

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_delete_post():
    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 200, (
        f"Expected status code 200, but received "
        f"{response.status_code}: {response.text}"
    )    assert "id" in data


def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body content.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
