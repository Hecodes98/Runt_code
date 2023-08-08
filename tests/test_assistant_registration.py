from Utils.page_factory import PageFactory
from Utils.save_screenshots import SaveScreenshots
from config import BASE_URL, ASSISTANT_BASE
from pytest_check import check
from assertpy import assert_that
import pytest
import time

class TestAssistantRegistration:
    def base_test(self, driver, username, password, document_number, ticket_number ,assistant_registration_page):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username, password)
        time.sleep(5)
        login_page.fill_inputs_and_click_login(username, password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_close_tutorial_button()
        home_page.click_menu_button()
        home_page.click_courses_menu_option()
        home_page.click_attendee_registration_menu_option()
        assistant_registration_page.click_accept_modal_button()
        assistant_registration_page.click_document_type_select_input()
        assistant_registration_page.click_cc_option()
        assistant_registration_page.fill_document_number_textbox(document_number)
        assistant_registration_page.click_consult_button()
        time.sleep(5)
        assistant_registration_page.click_record_violation_button()
        time.sleep(5)
        assistant_registration_page.fill_ticket_number_textbox(ticket_number)
        time.sleep(5) #Botón buscar numero de comparendo, cuenta con un retraso propio de la página web, 
        #por eso se usa time.sleep(5) para este caso en especial, al quitar este time.sleep retorna error, que sería el comportamiento esperado
        assistant_registration_page.click_search_ticket_number_button()
    
    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "")])
    @pytest.mark.EP1_CUR01505
    def test_attendee_registration_field_enable_comparendo_number_field(self,driver, username, password, document_number, ticket_number):
        """
        Verifica que el mensaje de error al no ingresar datos aparezca y que el campo comparendo se habilite
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Número Comparendo es obligatorio") 
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP1_CUR01505")
        time.sleep(5)  

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "12345678901234567890")])
    @pytest.mark.EP2_CUR01505
    def test_attendee_registration_field_enable_infraction_number_field(self,driver, username, password, document_number, ticket_number):
        """
        Verifica que el campo de infracción se habilite luego de ingresar un numero de comparendo de 20 caractéres
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error no se muestre").is_equal_to("There's no error message") 
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP2_CUR01505")
        time.sleep(5)  

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "12345678901234567890")])
    @pytest.mark.EP3_CUR01505
    def test_attendee_registration_field_enable_comparendo_date(self,driver, username, password, document_number, ticket_number):
        """
        Verifica que el campo de fecha de comparendo se habilite luego de ingresar un numero de comparendo de 20 caractéres
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error no se muestre").is_equal_to("There's no error message") 
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP3_CUR01505")
        time.sleep(5)

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "12345678901234567890")])
    @pytest.mark.EP4_CUR01505
    def test_attendee_registration_field_enable_entity(self,driver, username, password, document_number, ticket_number):
        """
        Verifica que el campo de entidad se habilite luego de ingresar un numero de comparendo de 20 caractéres
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error no se muestre").is_equal_to("There's no error message") 
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP4_CUR01505")
        time.sleep(5)  

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "12345678901234567890")])
    @pytest.mark.EP5_CUR01505
    def test_attendee_registration_field_enable_transit_organism(self,driver, username, password, document_number, ticket_number):
        """
        Verifica que el campo de Organismo de Transito se habilite luego de ingresar un numero de comparendo de 20 caractéres
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error no se muestre").is_equal_to("There's no error message") 
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP5_CUR01505")
        time.sleep(5)  
    
    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "17345678901254267690")])
    @pytest.mark.EP7_CUR01505
    def test_attendee_registration_comparendo_not_registered(self,driver, username, password, document_number, ticket_number):
        """
        Validar que el comparendo no se encuentre registrado en esta u otro establecimiento. Funcionario CIA.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_infraction_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Infracción es obligatorio") 
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP7_CUR01505")
        time.sleep(5)

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "17345678901254267690")])
    @pytest.mark.EP8_CUR01505
    def test_attendee_registration_field_enable_all_fields(self,driver, username, password, document_number, ticket_number):
        """
        Validar que el sistema habilite la edición de campos, Funcionario CIA.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_infraction_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Infracción es obligatorio") 
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP8_CUR01505")
        time.sleep(5)

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "17345678901254267690")])
    @pytest.mark.EP9_CUR01505
    def test_attendee_registration_field_valid_info(self,driver, username, password, document_number, ticket_number):
        """
        Validar que la información suministrada cumpla con las condiciones descritas. Funcionario CIA.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_infraction_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Infracción es obligatorio") 
        time.sleep(3)
        assistant_registration_page.click_infraction_input()
        assistant_registration_page.click_infraction_input_option_1()
        assistant_registration_page.send_comparendo_date("11/4/2023") #TODO, ACLARAR QUE LA PAGINA CUENTA CON UN BUG, PERMITE FECHAS DE COMPARENDO FUTURAS, COMPORTAMIENTO NO PERMITIDO
        assistant_registration_page.click_entity_input()
        assistant_registration_page.click_entity_input_option_1()
        assistant_registration_page.click_transit_authority_input()
        assistant_registration_page.click_transit_authority_input_option_1()
        assistant_registration_page.click_modal_button_infraction_registration()
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP9_CUR01505")
        time.sleep(5)

    """@pytest.mark.EP10_CUR01505 no se especifica el test
        Con este ID ya que se valida esto en cada test
    """

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477902", "1qazxsw2.24","12345678", "17345678901254267690")])
    @pytest.mark.EP11_CUR01505
    def test_attendee_registration_comparendo_already_exists(self,driver, username, password, document_number, ticket_number):
        """
        Validar cuando el comparendo ya esta registrado o con un curso asociado. Funcionario CIA.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_infraction_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Infracción es obligatorio") 
        time.sleep(3)
        assistant_registration_page.click_infraction_input()
        assistant_registration_page.click_infraction_input_option_1()
        assistant_registration_page.send_comparendo_date("11/4/2023") #TODO, ACLARAR QUE LA PAGINA CUENTA CON UN BUG, PERMITE FECHAS DE COMPARENDO FUTURAS, COMPORTAMIENTO NO PERMITIDO
        assistant_registration_page.click_entity_input()
        assistant_registration_page.click_entity_input_option_1()
        assistant_registration_page.click_transit_authority_input()
        assistant_registration_page.click_transit_authority_input_option_1()
        assistant_registration_page.click_modal_button_infraction_registration()
        time.sleep(2) # Se usan estos helpers por el momento por demoras con la UI que genera angular
        assistant_registration_page.click_record_violation_button()
        time.sleep(2) # Se usan estos helpers por el momento por demoras con la UI que genera angular
        assistant_registration_page.fill_ticket_number_textbox_modal_2(ticket_number)
        time.sleep(5) #Botón buscar numero de comparendo, cuenta con un retraso propio de la página web, 
        #por eso se usa time.sleep(5) para este caso en especial, al quitar este time.sleep retorna error, que sería el comportamiento esperado
        assistant_registration_page.click_search_ticket_number_button()
        SaveScreenshots.save_screenshot(driver, ASSISTANT_BASE, "EP11_CUR01505")
        time.sleep(5)


