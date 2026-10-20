from playwright.sync_api import Locator, Page


class InventoryPage:
    """商品一覧の画面"""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.items = page.locator(".inventory_item")
        self.cart_badge: Locator = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_button(self, product: str) -> Locator:
        """追加ボタン。product は商品名をハイフンでつないだもの（例：sauce-labs-backpack）"""
        return self.page.locator(f"[data-test='add-to-cart-{product}']")

    def remove_button(self, product: str) -> Locator:
        """削除ボタン（追加すると、追加ボタンと入れ替わる）"""
        return self.page.locator(f"[data-test='remove-{product}']")

    def add_to_cart(self, product: str) -> None:
        self.add_button(product).click()

    def open_cart(self) -> None:
        self.cart_link.click()
