from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.search_information_page import SearchInformationPage
from pages.organizations_page import OrganizationsPage
from pages.facility_manager import FacilityManagerPage
from pages.instructor_page import InstructorPage
from pages.assistant_registration import AssistantRegistrationPage
from pages.scheduling_page import SchedulingPage


class PageFactory:
    @staticmethod
    def create_page(driver, page_name):
        if page_name == "login":
            return LoginPage(driver)
        if page_name == "home":
            return HomePage(driver)
        if page_name == "search_info":
            return SearchInformationPage(driver)
        if page_name == "organizations":
            return OrganizationsPage(driver)
        if page_name == "facility_manager":
            return FacilityManagerPage(driver)
        if page_name == "instructor_page":
            return InstructorPage(driver)
        if page_name == "assistant_registration":
            return AssistantRegistrationPage(driver)
        if page_name == "scheduling":
            return SchedulingPage(driver)
        else:
            raise ValueError("Page not found: " + page_name)
