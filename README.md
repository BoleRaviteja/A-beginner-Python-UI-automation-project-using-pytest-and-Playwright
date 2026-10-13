# SauceDemo UI Automation Testing

A beginner-friendly UI automation project built with **Python, Playwright, and pytest**, using the **Page Object Model (POM)** design pattern.

The project automates key user journeys on the [SauceDemo](https://www.saucedemo.com/) web application, including login validation, shopping cart behavior, and checkout.

## Project Objectives

- Practice browser automation using Playwright and Python.
- Organize automation code using the Page Object Model.
- Validate positive and negative application scenarios.
- Use pytest fixtures for reusable test setup.
- Generate HTML test reports, screenshots, and video recordings.
- Run automated tests through GitHub Actions CI.

## Tech Stack

- **Language:** Python 3.13
- **Automation:** Playwright
- **Test framework:** pytest
- **Browser:** Chromium
- **Reporting:** pytest-html
- **CI:** GitHub Actions

## Project Structure

```text
Saucedemo_Testing/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── reports/                 # HTML report and per-test browser evidence
├── conftest.py              # Shared fixtures
├── pyproject.toml           # pytest configuration
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── tests.yml        # GitHub Actions workflow
└── README.md
```

## Test Coverage

### Login Tests

- Login with valid credentials and verify the inventory page is visible.
- Reject an unknown username or incorrect password.
- Reject a locked-out user.
- Validate empty username and empty password messages.

### Shopping Cart Tests

- Add Sauce Labs Backpack and verify the cart badge, product name, and price.
- Remove the backpack and verify the product row and cart badge disappear.
- Add two products and verify both cart names and badge count `2`.
- Remove one of two products and verify the remaining item and badge count `1`.
- Continue shopping and reopen the cart to verify its contents persist.

### Checkout Tests

- Validate required first name, last name, and postal code.
- Complete a purchase and verify the order confirmation.

There are currently **15 Chromium test cases**. Assertions check application outcomes, not only whether actions completed.

## Architecture

### Page Object Model

Page classes in `pages/` contain selectors and reusable UI actions:

- `LoginPage`: login form interactions and error messages.
- `InventoryPage`: product list, product selection, and cart navigation.
- `CartPage`: cart item locators, backpack removal, and checkout navigation.
- `CheckoutPage`: checkout form interactions and order confirmation.

Tests in `tests/` describe scenarios and assert the expected behavior. This separation keeps selectors and interactions reusable while making test intent easy to read.

### Fixtures

The root `conftest.py` provides shared page-object fixtures and an authenticated inventory fixture. The `page` fixture is supplied by pytest-playwright, which manages browser, context, and page setup and teardown.

## Setup and Installation

### 1. Clone the repository

```powershell
git clone https://github.com/BoleRaviteja/A-beginner-Python-UI-automation-project-using-pytest-and-Playwright.git
cd A-beginner-Python-UI-automation-project-using-pytest-and-Playwright
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies and Chromium

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

If activation is unavailable, use the environment's Python executable directly:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m playwright install chromium
```

## Running the Tests

Run the complete suite:

```powershell
python -m pytest -v
```

Run explicitly with Chromium:

```powershell
python -m pytest -v --browser chromium
```

Run with a visible browser:

```powershell
python -m pytest tests/ -v --headed
```

Run a specific test:

```powershell
python -m pytest "tests/test_cart.py::test_backpack_can_be_removed_from_cart" -v
```

The default pytest configuration captures screenshots and videos and generates a self-contained HTML report on every run. To retain screenshots and videos only when a test fails, override the defaults:

```powershell
python -m pytest tests/ -v --screenshot=only-on-failure --video=retain-on-failure
```

## Test Reports and Artifacts

The configured output directory is `reports/`:

- **HTML report:** `reports/report.html`
- **Screenshots:** Per-test folders, for example `reports/tests-test-cart-py-test-backpack-is-added-to-cart-chromium/`
- **Videos:** `video.webm` files in per-test folders

Open `reports/report.html` in a browser to review the latest run. Each subsequent run updates the report and browser evidence.

## Continuous Integration

The GitHub Actions workflow is [.github/workflows/tests.yml](.github/workflows/tests.yml). It runs on pushes and pull requests, installs Python dependencies and Chromium, and executes the suite headlessly. The `reports/` directory is uploaded as the `playwright-test-results` artifact even if tests fail; GitHub retains the artifact for 14 days.

The last verified workflow run on `main` passed all 12 tests before the latest two cart scenarios were added locally. Separate red historical runs were created intentionally to verify failure reporting and artifact upload; they do not represent failures on the current `main` branch.

## Latest Local Test Result

**15 tests passed** using Chromium in 33.67 seconds.

```powershell
python -m pytest -v --browser chromium
```

The local test result and hosted CI result describe those specific runs; passing tests do not prove the application is defect-free.

## Future Improvements

- Add more cart edge cases, such as verifying the cart remains empty after removing all items.
- Expand checkout scenarios and assertions.
- Add cross-browser coverage where appropriate.
- Improve reusable test data and configuration as the suite grows.

## Author

**Raviteja Bole**

GitHub: [BoleRaviteja](https://github.com/BoleRaviteja)

---

*A learning project for practicing Python-based UI automation, pytest, Playwright, and maintainable test design.*
