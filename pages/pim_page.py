from playwright.sync_api import Page, expect
from pages.pim.add_employee_page import AddEmployeePage

class PIMPage:

    def __init__(self, page: Page):
        self.page : Page = page

        self.pim_menu_item =  page.get_by_role("link", name = "PIM")
        self.pim_heading = page.get_by_role("heading" , name="PIM")
        self.add_employee_button = page.get_by_text("Add Employee")
        
        self.pim_menu_item.click()
        expect(self.pim_heading).to_be_visible()

    def navigate(self):
        self.pim_menu_item.click()
        return self

    def is_loaded(self):
        expect(self.pim_heading).to_be_visible()
        return self

    def check_PIM_title_is_visiable(self):
    
        expect(self.pim_heading).to_be_visible()


    def go_to_add_employee_page(self):
        
        self.add_employee_button.click()
        expect(self.page.get_by_role("heading", name="Add Employee")).to_be_visible()
        
        return AddEmployeePage(self.page)

    def go_to_employee_list_page(self):
            self.page.get_by_role("link", name="Employee List").click()
            expect(self.page.get_by_role("heading", name="Employee Information")).to_be_visible()

            