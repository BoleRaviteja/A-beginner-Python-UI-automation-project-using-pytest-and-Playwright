import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def _open_checkout(
    inventory_page: InventoryPage, cart_page: CartPage
) -> None:
    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.checkout()


@pytest.mark.parametrize(
    ("first_name", "last_name", "postal_code", "error_message"),
    [
        ("", "Lovelace", "12345", "Error: First Name is required"),
        ("Ada", "", "12345", "Error: Last Name is required"),
        ("Ada", "Lovelace", "", "Error: Postal Code is required"),
    ],
    ids=["first-name-required", "last-name-required", "postal-code-required"],
)
def test_checkout_requires_customer_details(
    authenticated_inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
    first_name: str,
    last_name: str,
    postal_code: str,
    error_message: str,
) -> None:
    _open_checkout(authenticated_inventory_page, cart_page)
    checkout_page.fill_customer_information(first_name, last_name, postal_code)

    checkout_page.continue_to_overview()

    expect(checkout_page.error_message).to_have_text(error_message)


def test_customer_can_complete_purchase(
    authenticated_inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
) -> None:
    _open_checkout(authenticated_inventory_page, cart_page)
    checkout_page.fill_customer_information("Ada", "Lovelace", "12345")
    checkout_page.continue_to_overview()
    checkout_page.finish_order()

    expect(checkout_page.confirmation_message).to_be_visible()