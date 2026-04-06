import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.pim.add_employee_page import AddEmployeePage
import pytest


def test_login_valid(page:Page):
    loginPage = LoginPage(page)

    loginPage.login_with_valid_admin()

@pytest.mark.parametrize("username,password",[
    ("admin", "1234443"),
    ("add", "23eee"),
    ("33ee", "admin123"),
    ])    
def test_login_invalid(page:Page, username, password):
    login_page = LoginPage(page)
    login_page.login_with_invalid_admin(username=username, password=password)    
