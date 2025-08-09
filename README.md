# Selenium Automated Tests - The Internet

This project contains automated UI tests developed with Selenium WebDriver and pytest, targeting [The Internet](https://the-internet.herokuapp.com/) website.

## Overview

- Tests cover key UI components such as login forms, checkboxes, dropdowns, alerts, frames, dynamic controls, multiple windows, drag & drop, and file upload.  
- Uses explicit waits and best practices for reliable test execution.  
- Designed as a learning and demonstration project for Selenium automation.

## Requirements

- Python 3.x  
- Selenium  
- pytest  
- Microsoft Edge WebDriver (configured in `conftest.py`)

## Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/pedrohli-work/python-selenium-app1-LearningSelenium

2. Create and activate a Python virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Download the appropriate Microsoft Edge WebDriver from here and update the path in conftest.py.

5. Run tests with:
    pytest

Structure
conftest.py: Contains pytest fixtures for WebDriver setup and teardown.

Test scripts named by feature, e.g. test_login_positive.py, test_checkboxes.py.

Tests use explicit waits (WebDriverWait) to synchronize and assertions to validate expected results.

Notes
WebDriver executables, virtual environments (venv), and Python cache files (__pycache__) are ignored via .gitignore.

Large files like test videos or screenshots should be stored externally and linked; avoid pushing them to the repo.

Author
PedroLi — Software Engineer focused on automation and testing.