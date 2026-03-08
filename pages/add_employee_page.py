from playwright.async_api import Page

class AddEmployeePage:

    def __init__(self, page:Page):
        self.page: Page = page
        self.add_employee_heading = page.get_by_role("heading", name="Add Employee")
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.middle_name = page.get_by_role("textbox", name="Middle Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")

        self.login_details_switch = page.locator(".oxd-switch-input")


        self.username_login =  page.get_by_role("textbox").nth(5)

        self.password_login  =  page.locator("input[type=\"password\"]").first

        self.password_confirmation_login =    page.locator("input[type=\"password\"]").nth(1)

        self.save_button = page.get_by_role("button", name="Save")

    def create_employee(self,firstname: str, midllename: str, lastname: str):
        self.first_name.fill(firstname)
        self.middle_name.fill(midllename)
        self.last_name.fill(lastname)
        
        self.save_details()

    def create_employee_with_login_details(self,firstname: str, midllename: str, lastname: str,username: str, password: str):
        self.first_name.fill(firstname)
        self.middle_name.fill(midllename)
        self.last_name.fill(lastname)
        self.login_details_switch.click()
        self.username_login.fill(username)
        self.password_login.fill(password)
        self.password_confirmation_login.fill()

        self.save_details()

    def save_details(self):
        self.save_button.click()

