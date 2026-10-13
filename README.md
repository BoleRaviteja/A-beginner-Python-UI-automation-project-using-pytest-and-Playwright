# Playwright QA Practice

A Python UI automation project using pytest and Playwright to test SauceDemo login, cart, and checkout workflows. The tests use a Page Object Model so page selectors and browser actions are kept separate from test scenarios.

## Setup (Windows PowerShell)

From this project folder, run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install
```

If PowerShell blocks virtual environment activation, use the environment's Python directly instead:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\playwright.exe install
```

## Run the test

```powershell
python -m pytest -v
```

To watch the browser while it runs:

```powershell
python -m pytest -v --headed
```

Every test run captures screenshots and videos and generates an HTML test report. Outputs are organized here:

- `reports/report.html`: self-contained pytest-html report with environment, summary, and per-test results.
- `reports/`: per-test folders containing screenshots and `video.webm` recordings.

Open `reports/report.html` in a browser to review the latest run. These generated outputs are replaced or updated by the next run.

## Project structure

```text
pages/                  Page objects and UI actions
conftest.py             Shared Playwright page-object fixtures
tests/test_login.py     Negative login scenarios
tests/test_cart.py      Cart item and price checks
tests/test_checkout.py  Required-field and successful-purchase tests
reports/                Generated HTML report, screenshots, and videos
```

`page` is a browser-page fixture supplied by pytest-playwright. Page objects contain selectors and actions; tests use Playwright's `expect` assertions to verify outcomes. These assertions wait for the expected state, so fixed sleeps are unnecessary.

## Run selected tests

```powershell
python -m pytest tests/test_login.py -v
python -m pytest tests/test_checkout.py -v
python -m pytest tests/test_cart.py -v --headed
```

## Learning workflow

1. Run the test and confirm it passes.
2. Change one expected value temporarily and observe the failure output.
3. Add another scenario as a focused test, such as removing the backpack.
4. Put reusable page interactions in the matching page object.
5. When a test fails, use the assertion message and rerun the failing test with `--headed` to inspect the browser behavior.
