from playwright.sync_api import Page


class CartPage:
    """カート画面"""

    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")

    def checkout(self) -> None:
        self.checkout_button.click()
