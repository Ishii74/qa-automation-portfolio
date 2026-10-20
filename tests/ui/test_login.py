# tests/test_login.py
import re

from playwright.sync_api import Page, expect

from conftest import LOCKED_OUT_USER, PASSWORD, STANDARD_USER
from pages.login_page import LoginPage


def test_tc01_login_success(page: Page, login_page: LoginPage):
    """TC-01（FV-09-C, FV-13-C）正しいID/PWでログインすると、商品一覧が表示される"""
    login_page.login(STANDARD_USER, PASSWORD)

    expect(page).to_have_url(re.compile(r"/inventory\.html$"))


def test_tc02_login_wrong_password(page: Page, login_page: LoginPage):
    """TC-02（FV-01-C）パスワードが誤っているとログインできず、エラーが表示される"""
    login_page.login(STANDARD_USER, "wrong_password")

    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text(
        "Username and password do not match"
    )
    # ログイン画面のままで、遷移していない
    expect(page).not_to_have_url(re.compile(r"/inventory\.html"))
    expect(login_page.login_button).to_be_visible()


def test_tc03_login_locked_out_user(page: Page, login_page: LoginPage):
    """TC-03（FV-02-C）ロックされたユーザーはログインできず、ロックのエラーが表示される"""
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text("locked out")
    expect(page).not_to_have_url(re.compile(r"/inventory\.html"))
    expect(login_page.login_button).to_be_visible()


def test_tc48_login_unknown_user(page: Page, login_page: LoginPage):
    """TC-48（FV-03-C）存在しないユーザー名ではログインできず、エラーが表示される"""
    login_page.login("unknown_user", PASSWORD)

    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text(
        "Username and password do not match"
    )
    expect(page).not_to_have_url(re.compile(r"/inventory\.html"))
    expect(login_page.login_button).to_be_visible()


def test_tc49_login_empty_username(page: Page, login_page: LoginPage):
    """TC-49（FV-10-C）ユーザー名が空だとログインできず、必須エラーが表示される"""
    login_page.login("", PASSWORD)

    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text("Username is required")
    expect(page).not_to_have_url(re.compile(r"/inventory\.html"))
    expect(login_page.login_button).to_be_visible()


def test_tc50_login_empty_password(page: Page, login_page: LoginPage):
    """TC-50（FV-11-C）パスワードが空だとログインできず、必須エラーが表示される"""
    login_page.login(STANDARD_USER, "")

    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text("Password is required")
    expect(page).not_to_have_url(re.compile(r"/inventory\.html"))
    expect(login_page.login_button).to_be_visible()
