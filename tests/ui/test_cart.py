# tests/test_cart.py
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage

BACKPACK = "sauce-labs-backpack"


def test_tc17_add_item_badge_count(inventory_page: InventoryPage):
    """TC-17（FV-14-C）商品を追加すると、カートの件数が1になる"""
    # 追加前は、バッジが出ていない（0件）
    expect(inventory_page.cart_badge).to_have_count(0)

    inventory_page.add_to_cart(BACKPACK)

    expect(inventory_page.cart_badge).to_have_text("1")


def test_tc18_add_item_button_change(inventory_page: InventoryPage):
    """TC-18（FV-14-C）商品追加後、ボタンが「Remove」に変わる"""
    inventory_page.add_to_cart(BACKPACK)

    expect(inventory_page.remove_button(BACKPACK)).to_have_text("Remove")
    # 追加ボタンは、削除ボタンに入れ替わっている
    expect(inventory_page.add_button(BACKPACK)).to_have_count(0)
