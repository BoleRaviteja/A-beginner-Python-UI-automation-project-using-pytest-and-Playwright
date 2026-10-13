from playwright.sync_api import Locator, Page


class CheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def error_message(self) -> Locator:
        return self.page.locator('[data-test="error"]')

    @property
    def confirmation_message(self) -> Locator:
        return self.page.get_by_text("Thank you for your order!")

    def fill_customer_information(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        self.page.locator('[data-test="firstName"]').fill(first_name)
        self.page.locator('[data-test="lastName"]').fill(last_name)
        self.page.locator('[data-test="postalCode"]').fill(postal_code)

    def continue_to_overview(self) -> None:
        self.page.locator('[data-test="continue"]').click()

    def finish_order(self) -> None:
        self.page.locator('[data-test="finish"]').click()