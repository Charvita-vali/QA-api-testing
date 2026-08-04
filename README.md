# 🌐 QA API Testing — JSONPlaceholder

A self-directed API testing project built to practice REST API testing using **Python**, **pytest**, and **requests**. This project validates CRUD operations against the JSONPlaceholder REST API and demonstrates API validation, response verification, reusable test design, and automated test execution following QA best practices.

---

## 🎯 Project Goals

- Practice automated REST API testing using Python and pytest
- Validate CRUD operations (GET, POST, PUT, DELETE)
- Verify HTTP status codes, response headers, response body, and response time
- Build reusable and maintainable API test scripts
- Demonstrate API testing skills for Junior QA / SDET roles

---

## 🛠️ Tech Stack

- Python 3.12
- pytest
- requests
- JSONPlaceholder REST API
- Git & GitHub

---

## 📂 Project Structure

```
QA-api-testing
├── README.md
├── config.py                  # Base URL and request timeout
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Project dependencies
└── tests/
    └── test_posts.py          # Automated API test suite
```

---

## 🧪 Test Coverage

| Test Scenario | Endpoint | Validation Performed |
|---------------|----------|----------------------|
| Retrieve Single Post | GET /posts/1 | Status code, response body, data types, response headers, response time |
| Retrieve Non-Existing Post | GET /posts/9999 | Verify HTTP 404 response |
| Create New Post | POST /posts | Status code, request payload, response body, generated ID |
| Update Existing Post | PUT /posts/1 | Status code and updated response fields |
| Delete Existing Post | DELETE /posts/1 | Successful deletion (HTTP 200) |

### API Validations Performed

- HTTP Status Code Validation
- Response Header Validation
- Response Body Validation
- JSON Data Type Validation
- Response Time Validation
- CRUD Operation Testing
- Positive API Testing
- Negative API Testing

---

## ⚙️ Test Execution

All API tests were executed using **pytest**.

Run the test suite:

```bash
pytest
```

Example output:

```
============================ test session starts ============================

collected 5 items

tests/test_posts.py::test_get_single_post PASSED
tests/test_posts.py::test_get_post_not_found PASSED
tests/test_posts.py::test_create_post PASSED
tests/test_posts.py::test_update_post PASSED
tests/test_posts.py::test_delete_post PASSED

============================= 5 passed =============================
```

---

## 🌍 Application Under Test

**API:** https://jsonplaceholder.typicode.com

Resource tested:

- `/posts`

---

## 💡 Skills Demonstrated

- REST API Testing
- HTTP Methods (GET, POST, PUT, DELETE)
- API Request & Response Validation
- HTTP Status Code Validation
- JSON Response Validation
- Response Header Validation
- Response Time Validation
- Positive & Negative Testing
- Automated Test Execution
- Python Programming
- pytest Framework
- requests Library
- Git & GitHub Documentation

---

## 🏆 Key Achievements

- Designed and implemented 5 automated API test cases covering CRUD operations.
- Validated HTTP status codes, JSON response structure, response headers, and response time.
- Improved test maintainability using reusable configuration.
- Structured the project following pytest best practices.
- Successfully executed all automated tests with **100% pass rate**.

---

## 📊 Project Metrics

| Metric | Value |
|--------|-------|
| API Resources Tested | 1 |
| Endpoints Tested | 5 |
| Test Cases Automated | 5 |
| Test Cases Passed | 5/5 (100%) |
| HTTP Methods Covered | GET, POST, PUT, DELETE |
| Framework | pytest |
| Programming Language | Python 3.12 |

---

## 🚀 Future Enhancements

- Add PATCH endpoint testing
- Validate response schema using JSON Schema
- Add authentication API testing using Bearer Tokens
- Implement API testing with Postman collections
- Generate HTML test reports
- Integrate GitHub Actions for CI/CD pipeline
- Add data-driven API testing using pytest parameterization

---

## 📝 Notes

This is a personal learning project created to demonstrate REST API testing skills using Python.

JSONPlaceholder is a publicly available fake REST API intended for learning, testing, and prototyping purposes.

This project is not affiliated with or endorsed by JSONPlaceholder.

---

## 🔗 Related Projects

- **Project 1:** Manual QA Testing – SauceDemo E-Commerce Application
- **Project 3:** UI Automation Testing – SauceDemo (Playwright)
