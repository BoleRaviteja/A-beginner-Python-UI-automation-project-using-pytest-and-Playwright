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


def test_backpack_can_be_removed_from_cart(
    authenticated_inventory_page: InventoryPage, cart_page: CartPage
) -> None:
    authenticated_inventory_page.add_backpack()
    authenticated_inventory_page.open_cart()

    expect(cart_page.backpack_name).to_have_text("Sauce Labs Backpack")
    expect(cart_page.cart_badge).to_have_text("1")
    cart_page.remove_backpack()

    expect(cart_page.backpack_item).to_have_count(0)
    expect(cart_page.cart_badge).to_have_count(0)


def test_cart_badge_and_contents_update_for_multiple_products(
    authenticated_inventory_page: InventoryPage, cart_page: CartPage
) -> None:
    authenticated_inventory_page.add_backpack()
    authenticated_inventory_page.add_bike_light()
    expect(authenticated_inventory_page.cart_badge).to_have_text("2")

    authenticated_inventory_page.open_cart()

    expect(cart_page.item_names).to_have_text(
        ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    )
    expect(cart_page.cart_badge).to_have_text("2")


def test_removing_one_product_keeps_remaining_item_and_updates_badge(
    authenticated_inventory_page: InventoryPage, cart_page: CartPage
) -> None:
    authenticated_inventory_page.add_backpack()
    authenticated_inventory_page.add_bike_light()
    authenticated_inventory_page.open_cart()

    expect(cart_page.cart_badge).to_have_text("2")
    cart_page.remove_backpack()

    expect(cart_page.item_names).to_have_text(["Sauce Labs Bike Light"])
    expect(cart_page.cart_badge).to_have_text("1")


def test_cart_contents_persist_after_continuing_shopping(
    authenticated_inventory_page: InventoryPage, cart_page: CartPage
) -> None:
    authenticated_inventory_page.add_backpack()
    authenticated_inventory_page.open_cart()
    expect(cart_page.backpack_name).to_have_text("Sauce Labs Backpack")

    cart_page.continue_shopping()

    expect(authenticated_inventory_page.product_list).to_be_visible()
    expect(authenticated_inventory_page.cart_badge).to_have_text("1")
    authenticated_inventory_page.open_cart()

    expect(cart_page.backpack_name).to_have_text("Sauce Labs Backpack")
    expect(cart_page.cart_badge).to_have_text("1")