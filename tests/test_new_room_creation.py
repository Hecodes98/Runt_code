from selenium.webdriver.common.by import By
from Utils.page_factory import PageFactory
from Utils.save_screenshots import SaveScreenshots
from Utils.signature_process import SignatureProcess
from config import BASE_URL, NEW_ROOM_CREATION_BASE
from pytest_check import check
from assertpy import assert_that
import pytest
import time


class TestNewRoomCreation:

    def login(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477902", "1qazxsw2.24")
        time.sleep(5)
        login_page.fill_inputs_and_click_login("404477902", "1qazxsw2.24")
        
       

    def base(self,driver):
        self.login(driver)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_close_tutorial_button()
        home_page.click_menu_button()
        home_page.click_administration_menu_option()
        home_page.click_administration_organizations_button()

    def test_fill_textboxes_for_a_new_room_creation(self, driver):
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_new_room_button()
        facility_manager.fill_name_textbox("Hector Cardona")
        facility_manager.fill_capacity_textbox("2")
        facility_manager.click_save_button()
        facility_manager.click_accept_modal_button_twice()
        time.sleep(10)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        facility_manager.click_save_modal_button()
        
    @pytest.mark.EP2_CUR01504
    def test_validate_fields(self,driver):
        """
        Permite al organismo encargado, observar la pantalla con información precargada  con el nombre del establecimiento del 
        organismo de apoyo habilitado para dictar cursos comparendos al cual pertenece el funcionario autenticado así mismo como el módulo capacidad y Horario  mostrado en el prototipo A
        """
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_schedule_tab()
        SaveScreenshots.save_screenshot(driver, NEW_ROOM_CREATION_BASE, "EP2_CUR01504")
        time.sleep(5)
    """
    @pytest.mark.EP3_CUR01504 se obvea este test case ya que es el mismo de test case 'EP2_CUR01504' cuentan con una funcionalidad igual, lo que sería reescribir codigo innecesario
    """

    @pytest.mark.EP4_CUR01504
    def test_fill_textboxes_for_a_new_room_creation(self, driver):
        """
        Permite al organismo encargado crear y administrar una nueva sala, observando en pantalla campos de entrada para la creacion:
        -opción capacidad, Validando la capacidad máxima permitida y parametrizada por el sistema.
        Configurar salas.
        Guardar: el sistema muestra el mensaje de confirmacion de registro satisfactorio.
        """
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_new_room_button()
        facility_manager.fill_name_textbox("Hector Cardona")
        facility_manager.fill_capacity_textbox("2")
        facility_manager.click_save_button()
        facility_manager.click_accept_modal_button_twice()
        time.sleep(10)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process() 
        time.sleep(3)
        facility_manager.click_save_modal_button()
        SaveScreenshots.save_screenshot(driver, NEW_ROOM_CREATION_BASE, "EP2_CUR01504")
        time.sleep(5)
    
    @pytest.mark.EP5_CUR01504
    def test_fill_textboxes_and_validate_them(self, driver):
        """
        Permite al organismo validar el cumplimiento de las condiciones de los campos ingresados y almacenar la información con trazabilidad en el sistema registrando el log de auditoría
        """
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_new_room_button()
        facility_manager.fill_name_textbox("Hector Cardona")
        facility_manager.fill_capacity_textbox("cdgds")
        facility_manager.click_save_button()
        SaveScreenshots.save_screenshot(driver, NEW_ROOM_CREATION_BASE, "EP5_CUR01504")
        time.sleep(5)
    
    @pytest.mark.EP6_CUR01504
    def test_click_first_edit_button(self, driver):
        """
        Editar o eliminar la sala por el organismo autenticado seleccionando la opción Editar  permitiendo modificar la capacidad de sala, nombre, horario y aforo seleccionado, para posteriormente guardar la modificación 
        según el prototipo B de lo contrario seleccioa la opción existente para eliminar la sala ya creada. donde se muestra un mensaje de eliminación exitosa.
        """
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_first_edit_button()
        facility_manager.click_save_button()
        facility_manager.click_accept_modal_button_twice()
        time.sleep(10)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        facility_manager.click_save_modal_button()
        SaveScreenshots.save_screenshot(driver, NEW_ROOM_CREATION_BASE, "EP6_CUR01504")
        time.sleep(5)

    @pytest.mark.EP7_CUR01504
    def test_validate_unique_name(self, driver):
        """
        Permite al organismo validar los nombres de las salas y que estas no se encuentren repetidas en el sistema de ser así mostrará en pantalla el mensaje: <<ya existe una sala con el nombre de  la sala>>
        """
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_new_room_button()
        facility_manager.fill_name_textbox("Salón 1")
        facility_manager.fill_capacity_textbox("2")
        facility_manager.click_save_button()
        facility_manager.click_accept_modal_button_twice()
        time.sleep(10)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        time.sleep(3)
        facility_manager.click_save_modal_button()
        SaveScreenshots.save_screenshot(driver, NEW_ROOM_CREATION_BASE, "EP7_CUR01504")
        time.sleep(5)
    
    @pytest.mark.EP8_CUR01504
    def test_validate_over_quantity(self, driver):
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_new_room_button()
        facility_manager.fill_name_textbox("Salón 3")
        facility_manager.fill_capacity_textbox("10")
        facility_manager.click_save_button()
        facility_manager.click_accept_modal_button_twice()
        time.sleep(10)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        facility_manager.click_save_modal_button()
        SaveScreenshots.save_screenshot(driver, NEW_ROOM_CREATION_BASE, "EP8_CUR01504")
        time.sleep(5)

    @pytest.mark.EP9_CUR01504
    def test_validate_overwrote_schedule(self,driver):
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_schedule_tab()
        facility_manager.click_new_schedule_button()
        time.sleep(5)
        facility_manager.click_weekly_radio_button()
        time.sleep(5)
        facility_manager.click_day_select_input()
        time.sleep(5)
        facility_manager.click_sunday_option()
        time.sleep(5)
        facility_manager.click_init_minute_select_input()
        time.sleep(5)
        facility_manager.click_init_minute_option_1()
        time.sleep(5)
        facility_manager.click_init_time_select_input()
        time.sleep(5)
        facility_manager.click_init_time_option_2()
        time.sleep(5)
        facility_manager.click_meridian_select_input()
        time.sleep(5)
        facility_manager.click_meridian_option_1()

        facility_manager.click_end_minute_select_input()
        facility_manager.click_end_minute_option_1()
        facility_manager.click_end_time_select_input()
        facility_manager.click_end_time_option_1()
        facility_manager.click_end_meridian_select_input()
        facility_manager.click_end_meridian_option_1()
        facility_manager.click_save_button()
        facility_manager.click_accept_modal_button_twice()
        time.sleep(10)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        facility_manager.click_save_modal_button()
        SaveScreenshots.save_screenshot(driver, NEW_ROOM_CREATION_BASE, "EP9_CUR01504")
        time.sleep(10)

    """
    @pytest.mark.EP10_CUR01504,@pytest.mark.EP11_CUR01504, @pytest.mark.EP12_CUR01504
    se obvean porque en test pasados se testean repeditas veces
    """


    def validate_fields(self,driver):
        self.base(driver)
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_schedule_tab()
        facility_manager.click_new_schedule_button()
        time.sleep(5)
        facility_manager.click_diary_radio_button()
        facility_manager.click_day_select_input()
        facility_manager.click_monday_option()
        facility_manager.click_init_minute_select_input()
        facility_manager.click_init_minute_option_1()
        facility_manager.click_init_time_select_input()
        facility_manager.click_init_time_option_1()
        facility_manager.click_meridian_select_input()
        facility_manager.click_meridian_option_1()

        facility_manager.click_end_minute_select_input()
        facility_manager.click_end_minute_option_1()
        facility_manager.click_end_time_select_input()
        facility_manager.click_end_time_option_1()
        facility_manager.click_end_meridian_select_input()
        facility_manager.click_end_meridian_option_1()
        facility_manager.click_save_button()
        



    #@pytest.mark.parametrize("username, password", [("404477901", "1qazxsw2.")])
    #def test_organizations_validate_parametrized_date(self,driver, username, password):
        """
        Verifica que el mensaje de error al no ingresar datos aparezca
        """
    #    self.base_test(driver, username, password)
    #    organizations_page = PageFactory.create_page(driver,"organizations")
    #    time.sleep(10)
    #    organizations_page.click_organization_type_input()
    #    with check:
    #        assert_that(organizations_page.get_today_day_input()).described_as("Validar que la fecha que se muestre sea igual a la fecha de hoy menos los días parametrizados").is_not_none() 
    # 
    #    time.sleep(5)  

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


