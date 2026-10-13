from playwright.sync_api import Locator, Page


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def error_message(self) -> Locator:
        return self.page.locator('[data-test="error"]')

    @property
    def login_button(self) -> Locator:
        return self.page.locator('[data-test="login-button"]')

    def open(self) -> None:
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        self.page.locator('[data-test="username"]').fill(username)
        self.page.locator('[data-test="password"]').fill(password)
        self.page.locator('[data-test="login-button"]').click()