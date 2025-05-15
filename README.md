# Test Automation Framework

This project contains automated tests for both API and UI testing.

## Project Structure
```
├── tests/              # Test cases
│   ├── api/           # API tests
│   └── ui/            # UI tests
├── pages/             # Page Object Models
├── utils/             # Utility functions
├── fixtures/          # Test fixtures
├── config/            # Configuration files
├── conftest.py        # Pytest configuration
├── pytest.ini         # Pytest settings
└── requirements.txt   # Project dependencies
```

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your configuration:
```
API_BASE_URL=your_api_url
UI_BASE_URL=your_ui_url
```

## Running Tests
- Run all tests:
```bash
pytest
```

- Run with Allure report:
```bash
pytest --alluredir=./allure-results
allure serve ./allure-results
```

## Features
- API Testing with requests and jsonschema
- UI Testing with Selenium
- Allure reporting
- Environment configuration with dotenv
- Data generation with Faker
- Page Object Model pattern
- Fixtures for test setup and teardown 