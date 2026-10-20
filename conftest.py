import re

import pytest
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# SauceDemoの公開テストユーザー（サイト上に載っているもの）
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """ログイン画面を開いた状態の LoginPage（未ログイン）"""
    login = LoginPage(page)
    login.goto()
    return login


@pytest.fixture
def inventory_page(page: Page, login_page: LoginPage) -> InventoryPage:
    """standard_user でログイン済みの、商品一覧の InventoryPage（TC-05, TC-06の事前条件）"""
    login_page.login(STANDARD_USER, PASSWORD)
    expect(page).to_have_url(re.compile(r"/inventory\.html$"))
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)
