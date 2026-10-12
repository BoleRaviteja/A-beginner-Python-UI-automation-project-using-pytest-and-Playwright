# Playwright QA Practice

A beginner Python UI automation project using pytest and Playwright. The end-to-end test covers SauceDemo login, inventory and cart interactions, checkout, order completion, and logout.

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
- `reports/artifacts/`: per-test folders containing screenshots and `video.webm` recordings.

Open `reports/report.html` in a browser to review the latest run. These generated outputs are replaced or updated by the next run.

## End-to-end test

The test in `tests/test_full.py` logs in as `standard_user`, exercises inventory and cart interactions, completes checkout, and verifies that logout returns to the login page. `page` is a Playwright fixture supplied by pytest-playwright. Playwright's `expect` assertions wait for the page to reach the expected state, so fixed sleeps are unnecessary.

## Learning workflow

1. Run the test and confirm it passes.
2. Change one expected value temporarily and observe the failure output.
3. Add focused tests for invalid login and checkout validation.
4. When a test fails, use the assertion message and rerun with `--headed` to inspect the browser behavior.
