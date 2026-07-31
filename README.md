# QA API Testing — JSONPlaceholder

Automated API test suite using Python, `pytest`, and `requests`, testing [JSONPlaceholder](https://jsonplaceholder.typicode.com), a free fake REST API for testing and prototyping.

## Tech Stack
- Python 3.12
- pytest
- requests

## Test Coverage
- **GET** `/posts/1` — retrieve a single post, verify status code and response fields
- **GET** `/posts/9999` — verify 404 for a non-existent resource
- **POST** `/posts` — create a new post, verify status code 201 and returned data
- **PUT** `/posts/1` — update an existing post, verify updated fields in response
- **DELETE** `/posts/1` — verify successful deletion (status code 200)

## How to Run
1. Clone this repo
2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```
3. Install dependencies:
```bash
   pip install pytest requests
```
4. Run the tests:
```bash
   pytest -v
```

## Notes
This is a companion project to my manual testing ([qa-portfolio-saucedemo](https://github.com/Charvita-vali/QA-portfolio-saucedemo)) and UI automation ([qa-automation-saucedemo](https://github.com/Charvita-vali/QA-automation-saucedemo)) projects — together they demonstrate manual, UI automation, and API testing skills.