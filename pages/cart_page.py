from playwright.sync_api import Locator, Page


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def backpack_item(self) -> Locator:
        return self.page.locator('[data-test="inventory-item"]').filter(
            has_text="Sauce Labs Backpack"
        )

    @property
    def backpack_name(self) -> Locator:
        return self.backpack_item.locator('[data-test="inventory-item-name"]')

    @property
    def backpack_price(self) -> Locator:
        return self.backpack_item.locator('[data-test="inventory-item-price"]')

    @property
    def cart_badge(self) -> Locator:
        return self.page.locator('[data-test="shopping-cart-badge"]')

    def remove_backpack(self) -> None:
        self.backpack_item.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        ).click()

    def checkout(self) -> None:
        self.page.locator('[data-test="checkout"]').click()