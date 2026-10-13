from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_rejects_unknown_username(login_page: LoginPage) -> None:
    login_page.open()
    login_page.login("unknown_user", "secret_sauce")

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_rejects_incorrect_password(login_page: LoginPage) -> None:
    login_page.open()
    login_page.login("standard_user", "incorrect_password")

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_rejects_locked_out_user(login_page: LoginPage) -> None:
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_login_accepts_valid_credentials(
    login_page: LoginPage, inventory_page: InventoryPage
) -> None:
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(inventory_page.product_list).to_be_visible()


def test_login_rejects_empty_username(login_page: LoginPage) -> None:
    login_page.open()
    login_page.login("", "secret_sauce")

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Username is required"
    )
    expect(login_page.login_button).to_be_visible()


def test_login_rejects_empty_password(login_page: LoginPage) -> None:
    login_page.open()
    login_page.login("standard_user", "")

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Password is required"
    )
    expect(login_page.login_button).to_be_visible()