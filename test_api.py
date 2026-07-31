import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data


def test_get_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/9999")

    assert response.status_code == 404


def test_create_post():
    payload = {
        "title": "QA Testing Post",
        "body": "This is a test post created via automated API testing.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "QA Testing Post"
    assert data["userId"] == 1
    assert "id" in data


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