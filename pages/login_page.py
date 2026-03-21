from playwright.sync_api import Page

class LoginPage:
  def __init__(self, page: Page):
    self.page : Page = page
    self.username = page.get_by_role("textbox", name= "username")
    self.password = page.get_by_role("textbox", name = "password")
    self.button = page.get_by_role("button", name="Login")



  def goto(self):
      self.page.goto(  
              "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",
              timeout=60000
      )


  def login(self,username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.button.click()


