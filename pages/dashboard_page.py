
from playwright.async_api import Page, expect

class DashboardPage:

    def __init__(self, page: Page):
        self.page: Page = page
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        self.pim_menu_item =  page.get_by_role("link", name = "PIM")


    def check_dashboard_is_visable(self):
        expect(self.dashboard_heading).to_be_visible()


    
    def open_pim_page(self):
         
         self.pim_menu_item.click()
