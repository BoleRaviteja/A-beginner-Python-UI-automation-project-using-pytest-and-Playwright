from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_backpack_is_added_to_cart(
    authenticated_inventory_page: InventoryPage, cart_page: CartPage
) -> None:
    authenticated_inventory_page.add_backpack()
    expect(authenticated_inventory_page.cart_badge).to_have_text("1")

    authenticated_inventory_page.open_cart()

    expect(cart_page.backpack_name).to_have_text("Sauce Labs Backpack")
    expect(cart_page.backpack_price).to_have_text("$29.99")