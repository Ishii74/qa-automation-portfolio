# tests/test_checkout.py
import re

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def test_tc10_checkout_complete(
    page: Page,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
):
    """TC-10（FV-16-C）商品を1件入れて、購入者情報を入力して購入を完了できる"""
    # 1. 商品を1件追加して、カートを開く
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    expect(page).to_have_url(re.compile(r"/cart\.html$"))
    expect(cart_page.items).to_have_count(1)

    # 2. チェックアウトに進み、購入者情報（名・姓・郵便番号）を入力する
    cart_page.checkout()
    expect(page).to_have_url(re.compile(r"/checkout-step-one\.html$"))
    checkout_page.fill_info("Taro", "Yamada", "1000001")
    checkout_page.continue_()

    # 3. 確認画面で、選んだ商品が表示されていることを確認して、購入を確定する
    expect(page).to_have_url(re.compile(r"/checkout-step-two\.html$"))
    expect(checkout_page.item_names).to_have_text("Sauce Labs Backpack")
    checkout_page.finish()

    # 4. 購入完了のメッセージが表示される
    expect(page).to_have_url(re.compile(r"/checkout-complete\.html$"))
    expect(checkout_page.complete_header).to_have_text(
        "Thank you for your order!"
    )
