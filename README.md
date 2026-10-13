# Playwright QA Practice

A beginner Python UI automation project using pytest and Playwright. The first test covers logging into SauceDemo, adding Sauce Labs Backpack to the cart, and checking the cart contents and price.

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

## First test: add a product to the cart

- **Setup:** Start on SauceDemo's login page with an empty cart.
- **Actions:** Log in as `standard_user`, add Sauce Labs Backpack, and open the cart.
- **Expected:** The cart badge is `1`; the cart contains the backpack at quantity `1` and price `$29.99`.

The test is in `tests/test_cart.py`. `page` is a Playwright fixture supplied by pytest-playwright. Playwright's `expect` assertions wait for the page to reach the expected state, so fixed sleeps are unnecessary.

## Learning workflow

1. Run the test and confirm it passes.
2. Change one expected value temporarily and observe the failure output.
3. Add a separate test for removing the backpack.
4. Add tests for invalid login and checkout validation.
5. When a test fails, use the assertion message and rerun with `--headed` to inspect the browser behavior.
