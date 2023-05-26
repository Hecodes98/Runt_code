from selenium.webdriver.common.by import By
from Utils.page_factory import PageFactory
from Utils.signature_process import SignatureProcess
from pywinauto.application import Application
from config import BASE_URL
from pytest_check import check
from assertpy import assert_that
import pytest
import time


class TestLoginAndRegistration:
    def test_login(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        time.sleep(15)
        assert driver.current_url == "https://azspkdevstcus004.z19.web.core.windows.net/#/"

    def test_fill_violations_textboxes_and_click_search_button(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_search_information_option()
        home_page.click_violations_option()
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.click_select_input_type_document_cc()
        search_information_page.send_document_number("123456")
        search_information_page.send_ticket_initial_date("6/4/2001")
        search_information_page.send_ticket_final_date("10/4/2001")
        search_information_page.send_ticket_number("87654")
        search_information_page.click_search_button()
        time.sleep(10)
    
    def test_fill_organizations_textboxes_and_click_search(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_search_information_option()
        home_page.click_organizations_option()
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_cc()
        organizations_page.send_document_number('1088035775')
        organizations_page.send_commercial_registration_number('99887766')
        time.sleep(10)

    def test_fill_textboxes_for_a_new_room_creation(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_administration_menu_option()
        home_page.click_administration_organizations_button()
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_new_room_button()
        facility_manager.fill_name_textbox("Hector Cardona")
        facility_manager.fill_capacity_textbox("2")
        facility_manager.click_save_button()
        facility_manager.click_accept_modal_button_twice()
        time.sleep(5)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        facility_manager.click_save_modal_button()

    """  
    @pytest.mark.parametrize("username, password", [("404477901", "1qazxsw2."), ("404477902", "1qazxsw2."), 
                                                      ("404477904", "1qazxsw2."), ("404477905", "1qazxsw2."),
                                                      ("404477903", "1qazxsw2.")])
    def test_fill_textboxes_for_instructor_page(self,driver,username,password):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username, password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_administration_menu_option()
        home_page.click_instructor_administration_option()
        time.sleep(10)
        instructor_page = PageFactory.create_page(driver, "instructor_page")
        instructor_page.click_document_type_select_input()
        instructor_page.click_cc_option()
        instructor_page.fill_document_type_textbox("99887766")
    """


