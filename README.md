# 🚀 Hybrid QA Automation Framework (Python + Selenium + API + DB + CI/CD)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium)
![PyTest](https://img.shields.io/badge/PyTest-Framework-orange?logo=pytest)
![Allure](https://img.shields.io/badge/Allure-Reports-purple)
![FastAPI](https://img.shields.io/badge/FastAPI-Mock%20Server-teal?logo=fastapi)
![Postman](https://img.shields.io/badge/Postman-API%20Testing-orange?logo=postman)
![Newman](https://img.shields.io/badge/Newman-CLI-blue)
![SQLite](https://img.shields.io/badge/SQLite-DB-lightgrey?logo=sqlite)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI/CD-blue?logo=githubactions)
![CI](https://github.com/cyphermorgan/selenium-python-pytest-framework/actions/workflows/main.yml/badge.svg)
![Status](https://img.shields.io/badge/status-active-success)
![Tests](https://img.shields.io/badge/tests-automated-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-UI%20%7C%20API%20%7C%20DB-blue)
![Parallel](https://img.shields.io/badge/execution-parallel-informational)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A **production-style hybrid test automation framework** built using **Python, Selenium, PyTest, API testing, database validation, and CI/CD pipelines**.

This framework demonstrates how modern QA systems validate applications across **multiple layers**:

* UI (Frontend)
* API (Backend services)
* Database (Data integrity)

---

## 🔗 Live Reports
- Allure Report: https://cyphermorgan.github.io/selenium-python-pytest-framework/

# 🔥 Key Features

### 🖥️ UI Automation

* Selenium WebDriver
* Page Object Model (POM)
* Multi-browser support
* Screenshot capture on failure

### 🌐 API Testing

* Python-based API client
* Postman collection support
* Newman CLI execution
* API validation with structured logging

### 🗄️ Database Validation

* SQLite DB integration
* API vs DB validation tests
* Data integrity checks

### 🧪 Test Framework

* PyTest test runner
* Parametrized (data-driven) tests
* Retry mechanism for flaky tests
* Parallel execution (pytest-xdist)

### 📊 Reporting

* Allure Reports (rich UI)
* HTML reports
* Postman HTML reports

### ⚙️ Configuration Management

* YAML-based config system
* Environment support (`dev`, `staging`, etc.)
* CLI overrides (browser, env)

### 🧾 Logging

* Centralized logging system
* Logs for UI, API, DB layers

### 🚀 CI/CD Pipeline

* GitHub Actions integration
* Automated test execution
* Allure report deployment (GitHub Pages)
* Postman test execution via Newman

### 🧪 Mock API Server

* Built with FastAPI
* Ensures deterministic and reliable API tests

---

# 🧱 Project Structure

```bash
selenium-python-pytest-framework
│
├── tests/
│   ├── ui/
│   ├── api/
│   └── db/
│
├── pages/
│
├── framework/
│   ├── core/
│   ├── api/
│   ├── db/
│   └── utils/
│
├── mock_server/
│
├── postman/
│
├── config/
│
├── reports/
├── screenshots/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# 🧠 Framework Architecture

### UI Layer

Handles frontend automation using Selenium and Page Object Model.

### API Layer

Handles backend validation using:

* Python API client
* Postman + Newman

### DB Layer

Validates backend data using SQL queries.

### Integration Layer

Combines:

* API responses
* Database data
  to validate consistency across systems.

---

# ▶️ Running Tests

## 🔹 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Run all tests

```bash
pytest tests --env=dev
```

---

## 🔹 Run with parallel execution

```bash
pytest tests -n 4
```

---

## 🔹 Run specific layer

```bash
pytest tests/ui
pytest tests/api
pytest tests/db
```

---

# 📊 Reporting

## Allure Report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

👉 CI Report (GitHub Pages):
https://cyphermorgan.github.io/selenium-python-pytest-framework/

---

## Postman (Newman)

```bash
newman run postman/Hybrid_QA_API.postman_collection.json
```

HTML report:

```bash
reports/postman_report.html
```

---

# 🧪 Mock API Server

Run locally:

```bash
uvicorn mock_server.app:app --reload
```

Base URL:

```bash
http://127.0.0.1:8000
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically:

* Runs UI + API + DB tests
* Executes Postman collection
* Generates Allure report
* Deploys report to GitHub Pages

---

# 🔍 Example Test Flow

```text
Start CI pipeline
    ↓
Start Mock API
    ↓
Run PyTest (UI + API + DB)
    ↓
Run Postman (Newman)
    ↓
Validate API ↔ DB consistency
    ↓
Generate Allure report
    ↓
Deploy report to GitHub Pages
```

---

# 🚀 What This Project Demonstrates

* Real-world QA automation architecture
* Multi-layer validation strategy
* CI/CD integration
* Clean, scalable framework design
* Strong debugging & reporting practices

---

# 🔮 Future Enhancements

* Docker containerization
* Cross-browser grid execution (Selenium Grid)
* Allure + Newman report integration
* Performance testing integration
* Cloud execution (BrowserStack / Sauce Labs)

---

# 👤 Author

Built as a hands-on project to simulate a **real-world QA automation framework** used in modern engineering teams.

---

# ⭐ If you like this project

Give it a ⭐ and feel free to fork & extend it!