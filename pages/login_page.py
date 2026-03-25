from playwright.sync_api import Page, expect

class LoginPage:
  def __init__(self, page: Page):
    self.page : Page = page
  

  def login(self,username: str, password: str):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()


  def login_with_valid_admin(self):
     self.login(username="Admin", password="admin123")
    #  self.login_ok(self)
     dashboard_title = self.page.get_by_role("heading", name="Dashboard")

     expect(dashboard_title).to_be_visible  

  def login_with_invalid_admin(self, username , password):
     self.login(username=username, password=password)   

     expect(self.page.get_by_text("Invalid credentials")).to_be_visible()
  def verify_login_ok(self):
     
   
     dashboard_title = self.page.get_by_role("heading", name="Dashboard")

     expect(dashboard_title).to_be_visible     


