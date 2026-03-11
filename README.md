# Selenium Python PyTest Automation Framework

A simple UI automation framework built using **Selenium WebDriver, Python, and PyTest** following the **Page Object Model (POM)** design pattern.

The goal of this project is to demonstrate how a maintainable and scalable test automation framework can be structured while supporting **data-driven testing, reusable utilities, logging, and reporting**.

This repository was built as a practice project to simulate how UI automation frameworks are commonly organized in real QA environments.

---

# Features

* Selenium WebDriver automation
* PyTest test runner
* Page Object Model (POM)
* Data-driven testing using JSON
* Config-based environment setup
* Screenshot capture on test failure
* HTML test reports
* Logging for test execution
* Retry mechanism for flaky tests

---

# Tech Stack

* Python
* Selenium
* PyTest
* pytest-html
* webdriver-manager

---

# Project Structure

```id="pjh8rk"
selenium-python-pytest-framework
│
├── tests
│   └── test_login.py
│
├── pages
│   └── login_page.py
│
├── utilities
│   ├── base_class.py
│   ├── config_reader.py
│   ├── data_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   └── screenshot.py
│
├── data
│   └── login_test_data.json
│
├── config
│   └── config.json
│
├── logs
│
├── screenshots
│
├── reports
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Framework Design

The framework is organized into several layers to keep the code modular and maintainable.

### Test Layer

```id="e7e2y4"
tests/
```

Contains the test scenarios written using PyTest.
Tests validate application behavior using assertions and test data.

---

### Page Object Layer

```id="j8t4s7"
pages/
```

Implements the **Page Object Model** where each page contains:

* locators
* page actions
* interaction logic

This helps keep test cases clean and reduces duplication.

---

### Utilities Layer

```id="d8z0b1"
utilities/
```

Reusable helper modules used across the framework.

Examples include:

* **driver_factory** – initializes WebDriver
* **config_reader** – loads configuration values
* **data_reader** – loads test data
* **logger** – handles framework logging
* **screenshot** – captures screenshots when tests fail

---

### Test Data

```id="iv6d4o"
data/
```

Test data is stored in JSON format to support **data-driven testing**.

Example:

```id="a1hmy9"
{
  "username": "tomsmith",
  "password": "SuperSecretPassword!",
  "expected": "success"
}
```

---

### Configuration

```id="c7n3ve"
config/
```

Configuration values such as:

* base URL
* browser type
* wait time

are stored here to avoid hardcoding values throughout the code.

---

# Running the Tests

Clone the repository:

```id="ekc4ty"
git clone https://github.com/<your-username>/selenium-python-pytest-framework.git
```

Navigate into the project directory:

```id="g3zjpe"
cd selenium-python-pytest-framework
```

Install dependencies:

```id="n6s6yy"
pip install -r requirements.txt
```

Run the tests:

```id="skf4l8"
pytest
```

---

# Test Reporting

After execution, an HTML report is generated inside the `reports` folder.

Example:

```id="1waw8s"
reports/report.html
```

The report includes:

* test results
* execution duration
* failure details
* screenshots for failed tests

---

# Screenshot Capture

If a test fails, the framework automatically captures a screenshot.

Screenshots are saved inside:

```id="7r0dpt"
screenshots/
```

This helps with debugging and understanding test failures.

---

# Example Test Scenario

The framework currently includes a login test using a public demo site.

The following scenarios are covered:

* valid login
* invalid credentials
* empty username

Each test is executed using **PyTest parametrization** with data loaded from JSON.

---

# Example Test Flow

```id="5m2o0y"
pytest starts
      ↓
test data loaded from JSON
      ↓
browser launched via WebDriver
      ↓
page object interacts with UI
      ↓
assertions validate expected result
      ↓
logs and screenshots captured
      ↓
HTML report generated
```

---

# Future Improvements

Possible improvements that could be added:

* parallel test execution
* CI/CD integration
* Allure reporting
* environment switching (dev / staging / prod)
* API test support

---

# Author

Created as a practice project to explore building a structured Selenium test automation framework using Python and PyTest.