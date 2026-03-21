
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.pim.add_employee_page import AddEmployeePage



def test_add_empolyee_without_creds(page: Page, login_with_admin):
    
    pim = PIMPage(page).navigate() 
    addEmployee = pim.go_to_add_employee_page()
    addEmployee.create_employee(firstname="Marwan", midllename="Essam", lastname="Abdulhamid")

def test_add_empolyee_with_creds(page: Page, login_with_admin):
    pim = PIMPage(page).navigate() 
    addEmployee = pim.go_to_add_employee_page()
    addEmployee.create_employee_with_login_details(firstname="Marwan", midllename="Essam", lastname="Abdulhamid",username="marwan", password="123456789")
