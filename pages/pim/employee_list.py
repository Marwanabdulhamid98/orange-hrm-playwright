from playwright.sync_api import Page, expect
import pytest
class EmployeeListPage:

    def __init__(self,page:Page):
      self.page: Page = page

      self.employee_name =  (self.page.get_by_text("Employee Name")
                                            .locator("..")
                    
                                            .locator("..")
                                             .get_by_placeholder("Type for hints...")
                                            )
      self.employee_id =  (self.page.get_by_text("Employee Id")
                                            .locator("..")
                                            .locator("..")
                                            .locator(".oxd-input"))


      
  

 
    def search_valid_employee(self,name, id):
        self.employee_name.fill(name)
        self.employee_id.fill(id)
        self.page.get_by_role("button",name="Search").click()
        expect(self.page.get_by_role("row",name=name).first).to_contain_text(name)

         

    def search_invalid_employee(self,id, name):
        self.employee_name.fill(name)
        self.employee_id.fill(id)
        self.page.get_by_role("button",name="Search").click()
        expect(self.page.locator("span").filter(has_text="No Records Found")).to_be_visible()

    def deleteEmployee(self,name):
         self.search_valid_employee(name=name)
         self.page.locator(".oxd-table-cell-actions").locator(".oxd-icon-button").locator(".bi-trash").highlight()
                                  
      
                                    