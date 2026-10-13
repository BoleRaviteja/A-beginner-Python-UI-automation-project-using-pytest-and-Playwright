from playwright.sync_api import Locator, Page


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def product_list(self) -> Locator:
        return self.page.locator('[data-test="inventory-list"]')

    @property
    def cart_badge(self) -> Locator:
        return self.page.locator('[data-test="shopping-cart-badge"]')

    def add_backpack(self) -> None:
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def add_bike_light(self) -> None:
        self.page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()

    def open_cart(self) -> None:
        self.page.locator('[data-test="shopping-cart-link"]').click()