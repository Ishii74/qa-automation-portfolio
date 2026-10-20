from playwright.sync_api import Locator, Page


class LoginPage:
    """ログイン画面。ロケーターと操作を、ここに集める"""

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error: Locator = page.locator("[data-test='error']")

    def goto(self) -> None:
        self.page.goto("/")

    def login(self, username: str, password: str) -> None:
        """ID・パスワードを入れて、ログインを押す（空文字なら、その欄は空のまま）"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
