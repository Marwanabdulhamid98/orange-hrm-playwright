from playwright.sync_api import Page, expect

class AddEmployeePage:

    def __init__(self, page:Page):
        self.page: Page = page
        # self.add_employee_heading = page.get_by_role("heading", name="Add Employee")
        # self.first_name = page.get_by_role("textbox", name="First Name")
        # self.middle_name = page.get_by_role("textbox", name="Middle Name")
        # self.last_name = page.get_by_role("textbox", name="Last Name")
        
        self.first_name = page.get_by_placeholder("First Name")
        self.login_details_switch = page.locator(".oxd-switch-input")


        self.username_login =  page.get_by_role("textbox").nth(5)

        self.password_login  =  page.locator("input[type=\"password\"]").first

        self.password_confirmation_login =    page.locator("input[type=\"password\"]").nth(1)

        self.save_button = page.get_by_role("button", name="Save")

    def create_employee(self,firstname: str, midllename: str, lastname: str):
        self.page.get_by_placeholder("First Name").fill(firstname)
        self.page.get_by_placeholder("Middle Name").fill(midllename)
        self.page.get_by_placeholder("Last Name").fill(lastname)
        employee_id =  (self.page.get_by_text("Employee Id")
                                            .locator("..")
                                            .locator("..")
                                            .locator(".oxd-input"))
        
        init_id  = employee_id.input_value()
        final_id = init_id + "_99"
        employee_id.fill(final_id)
        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully saved")).to_be_visible()



    def create_employee_with_login_details(self,firstname: str, midllename: str, lastname: str,username: str, password: str):
        self.create_employee(firstname=firstname,midllename=midllename,lastname=lastname)
        self.login_details_switch.highlight()
        # self.username_login.fill(username)
        # self.password_login.fill(password)
        # self.password_confirmation_login.fill()

        # self.save_details()

    def save_details(self):
        self.save_button.click()

