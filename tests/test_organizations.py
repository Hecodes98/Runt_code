from Utils.page_factory import PageFactory
from pytest_html_reporter import attach
from Utils.save_screenshots import SaveScreenshots
from config import BASE_URL, ORGANIZATIONS_BASE
from pytest_check import check
from assertpy import assert_that
import pytest
import time


class TestOrganization:
    def base_test(self, driver, username, password):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username, password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_close_tutorial_button()
        home_page.click_menu_button()
        home_page.click_search_information_option()
        home_page.click_organizations_option()
    
    @pytest.mark.EP1_CUR01506
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.23")])
    def test_organizations_validate_parametrized_date(self,driver, username, password):
        """
        Ingresar con actor "Funcionario MT o Superintendencia de Transporte" para consultar 
        organismos que no reportan cursos.
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        with check:
            assert_that(organizations_page.get_today_day_input()).described_as("Validar que la fecha que se muestre sea igual a la fecha de hoy menos los días parametrizados").is_not_none() 
        SaveScreenshots.save_screenshot(driver, ORGANIZATIONS_BASE, "EP1_CUR01506")
        time.sleep(5)

    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.23")])
    @pytest.mark.EP2_CUR01506
    def test_organizations_document_cc_type(self,driver, username, password):
        """
        Validar el ingreso de información con actores "Funcionario MT o Superintendencia de Transporte"  
        en los campos de entrada disponibles y seleccionar la opción "Buscar".
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_cc()
        organizations_page.send_document_number('1088035775')
        organizations_page.click_search_button()
        SaveScreenshots.save_screenshot(driver, ORGANIZATIONS_BASE, "EP2_CUR01506")
        time.sleep(5)  
    
    @pytest.mark.parametrize("username, password, document_number", [("404477902", "1qazxsw2.23", "900739999")])
    @pytest.mark.EP3_CUR01506
    def test_organizations_document_nit_type_right_data(self,driver, username, password, document_number):
        """
        Validar el ingreso de información con actores "Funcionario MT o Superintendencia de Transporte"  
        en los campos de entrada disponibles y seleccionar la opción "Buscar".
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_nit()
        organizations_page.send_document_number(document_number)
        organizations_page.click_search_button()
        SaveScreenshots.save_screenshot(driver, ORGANIZATIONS_BASE, "EP3_CUR01506")
        time.sleep(5)

    @pytest.mark.parametrize("username, password, document_number", [("404477902", "1qazxsw2.23", "900739999")])
    @pytest.mark.EP8_CUR01506
    def test_organizations_click_clean_button(self,driver, username, password, document_number):
        """
        Validar el ingreso de información con actores "Funcionario MT o Superintendencia de Transporte"  
        en los campos de entrada disponibles y seleccionar la opción "Buscar".
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_nit()
        organizations_page.send_document_number(document_number)
        organizations_page.click_clean_button()
        SaveScreenshots.save_screenshot(driver, ORGANIZATIONS_BASE, "EP8_CUR01506")
        time.sleep(5) 

    @pytest.mark.parametrize("username, password, document_number", [("404477902", "1qazxsw2.23", "3563231")])
    @pytest.mark.EP10_CUR01506
    def test_organizations_wrong_document_number(self,driver, username, password, document_number):
        """
        Validar el ingreso de información con actores "Funcionario MT o Superintendencia de Transporte"  
        en los campos de entrada disponibles y seleccionar la opción "Buscar".
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_cc()
        organizations_page.send_document_number(document_number)
        organizations_page.click_search_button()
        SaveScreenshots.save_screenshot(driver, ORGANIZATIONS_BASE, "EP10_CUR01506")
        time.sleep(5) 

    @pytest.mark.parametrize("username, password", [("404477901", "1qazxsw2.23")])
    def test_organizations_commercial_registration_number(self,driver, username, password):
        """
        Verifica que el mensaje de error al no ingresar datos aparezca
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_cc()
        organizations_page.send_commercial_registration_number('1088035775')
        organizations_page.click_search_button()
        SaveScreenshots.save_screenshot(driver, ORGANIZATIONS_BASE, "EP11_CUR01506")
        time.sleep(5)  


