import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
 
@pytest.fixture(scope="function", autouse=True)
def goto(page: Page):
    """Fixture to navigate to the base URL."""
    base_url = "https://opensource-demo.orangehrmlive.com/"
    page.goto(base_url,  wait_until="domcontentloaded", 
                timeout=60000)
@pytest.fixture
def login_with_admin(page: Page):
    LoginPage(page).login_with_valid_admin()
# @pytest.fixture()
# def login_admin(page: Page, goto):
#     login_page = LoginPage()
#     login_page.login(username="admin", password="admin123")
#     return page
