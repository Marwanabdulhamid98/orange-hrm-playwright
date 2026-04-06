from playwright.sync_api import Page, expect
from pages.pim_page import PIMPage
import pytest
from pages.pim.employee_list import EmployeeListPage
from pages.pim.add_employee_page import AddEmployeePage


def test_search_valid(page:Page,login_with_admin):
      pimPage = PIMPage(page).navigate()
      pimPage.go_to_employee_list_page()
      pimPage.go_to_add_employee_page()
      addEmployeePage = AddEmployeePage(page)
      addEmployeePage.create_employee(firstname="Marwan",midllename="Issam",lastname="Abdulhamid")
      pimPage.go_to_employee_list_page()
      employeeListPage = EmployeeListPage(page)

      employeeListPage.search_valid_employee(name="Marwan",id="")
@pytest.mark.parametrize("name, id",[
       ("","00000"),
       ("test2", "990"),
       ("test3000", "")
   ]) 
def test_search_employee_invaild(page: Page, login_with_admin,name, id):
      pimPage = PIMPage(page).navigate()
      pimPage.go_to_employee_list_page()

      employeeListPage = EmployeeListPage(page)
      employeeListPage.search_invalid_employee(name=name,id=id)

