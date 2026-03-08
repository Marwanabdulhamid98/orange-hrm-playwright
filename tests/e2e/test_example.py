import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage



def test_add_employee_with_login_details(page):
    loginPage = LoginPage(page)
    loginPage.goto()
    loginPage.login(username="Admin", password="admin123")



    dashboardPage = DashboardPage(page)
    dashboardPage.check_dashboard_is_visable()
    dashboardPage.open_pim_page()


    pimPage = PIMPage(page)
    pimPage.check_PIM_title_is_visiable()
    pimPage.go_to_add_employee_page()



    addEmployeePage = AddEmployeePage(page)
    addEmployeePage.create_employee(firstname="marwan", midllename="Essam",lastname="Abdulhamid")
    
def test_add_employee(page):
    loginPage = LoginPage(page)
    loginPage.goto()
    loginPage.login(username="Admin", password="admin123")



    dashboardPage = DashboardPage(page)
    dashboardPage.check_dashboard_is_visable()
    dashboardPage.open_pim_page()


    pimPage = PIMPage(page)
    pimPage.check_PIM_title_is_visiable()
    pimPage.go_to_add_employee_page()



    addEmployeePage = AddEmployeePage(page)
    addEmployeePage.create_employee_with_login_details(firstname="marwan", midllename="Essam",lastname="Abdulhamid",username="marwan",password="admin123")
    

# def test_login_to_orangehrm(page: Page):

#     page.get_by_placeholder("Username").fill("Admin")
#     page.get_by_placeholder("Password").fill("admin123")

#     page.get_by_role("button", name="Login").click()
#     expect(page).to_have_title(re.compile("OrangeHRM"))

# def test_add_employee(page: Page):
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",timeout=30000)
#     page.get_by_role("textbox", name="Username").click()
#     page.get_by_role("textbox", name="Username").fill("admin")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("admin123")
#     page.get_by_role("button", name="Login").click()
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",timeout=60000)
#     page.get_by_role("link", name="PIM").click()
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList",timeout=60000)
#     page.get_by_role("button", name=" Add").click()
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee",timeout=60000)
#     page.get_by_role("textbox", name="First Name").click()
#     page.get_by_role("textbox", name="First Name").fill("mohammed")
#     page.get_by_role("textbox", name="Middle Name").click()
#     page.get_by_role("textbox", name="Middle Name").fill("ahmed")
#     page.get_by_role("textbox", name="Last Name").click()
#     page.get_by_role("textbox", name="Last Name").fill("mohammed")
#     page.get_by_role("button", name="Save").click()
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/181")
#     # page.get_by_role("heading", name="Personal Details").click() 
#     expect(page.locator("#app")).to_contain_text("Personal Details")

