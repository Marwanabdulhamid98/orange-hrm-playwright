from playwright.async_api import Page, expect


class PIMPage:

    def __init__(self, page: Page):
        self.page : Page = page

        self.pim_heading = page.get_by_role("heading" , name="PIM")
        self.add_employee_button = page.get_by_role("link", name="Add Employee")
       
    def check_PIM_title_is_visiable(self):
    
        expect(self.pim_heading).to_be_visible()


    def go_to_add_employee_page(self):
        
        self.add_employee_button.click()
        
   
        