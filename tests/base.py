from Utils.page_factory import PageFactory
from config import BASE_URL
import time

class BaseTest:
    def setup(self, driver):
        self.driver = driver
        self.login_page = PageFactory.create_page(self.driver, "login")
        self.home_page = PageFactory.create_page(self.driver, "home")
        self.search_information_page = PageFactory.create_page(self.driver, "search_info")
        self.organizations_page = PageFactory.create_page(self.driver,"organizations")
        self.facility_manager = PageFactory.create_page(self.driver, "facility_manager")
        self.instructor_page = PageFactory.create_page(self.driver, "instructor_page")
        self.driver.get(BASE_URL)
        self.login_page.fill_inputs_and_click_login(self.username, self.password)
        time.sleep(10)
