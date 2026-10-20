from playwright.sync_api import Page


class CheckoutPage:
    """購入手続きの画面（情報入力 → 確認 → 完了）"""

    def __init__(self, page: Page):
        self.page = page
        # 情報入力
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        # 確認
        self.item_names = page.locator(".inventory_item_name")
        self.finish_button = page.locator("[data-test='finish']")
        # 完了
        self.complete_header = page.locator("[data-test='complete-header']")

    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_(self) -> None:
        self.continue_button.click()

    def finish(self) -> None:
        self.finish_button.click()
