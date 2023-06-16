from config import BASE_URL, SCHEDULING_BASE
from Utils.page_factory import PageFactory
from Utils.save_screenshots import SaveScreenshots
from Utils.page_factory import PageFactory
from Utils.signature_process import SignatureProcess
from pytest_check import check
from assertpy import assert_that
import pytest
import time

class TestScheduling:

    def base(self, driver, username, password):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username, password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_close_tutorial_button()
        home_page.click_menu_button()
        home_page.click_courses_menu_option()
        home_page.click_courses_scheduling_option()
        time.sleep(15)

    @pytest.mark.base
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_base(self, driver, username, password):
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        time.sleep(2)
        scheduling_page.click_first_instructor_option()
        time.sleep(2)
        scheduling_page.click_accept_button()
        time.sleep(3)

    @pytest.mark.EP2_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP2_CUR01525(self, driver, username, password):
        """
        IMPORTANT: Los test del EP1 a EP4, EP11 estan contemplados en este test

        Validar que se muestren los campos que trae por defecto la "Hora inicio" y la "Hora fin" 
        de la franja horaria seleccionada en el calendario, son campos no editables.
        
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        time.sleep(2)
        with check:
            assert_that(scheduling_page.validate_order_of_rooms_list()).is_true()
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP2_CUR01525")
        time.sleep(5)


    @pytest.mark.EP4_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP4_CUR01525(self, driver, username, password):
        """
        IMPORTANT: Los test del EP1 a EP4, EP11, EP15 estan contemplados en este test

        Validar que se muestren los campos que trae por defecto la "Hora inicio" y la "Hora fin" 
        de la franja horaria seleccionada en el calendario, son campos no editables.
        
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        text_element = scheduling_page.validate_inputs_appears()
        with check:
            assert_that(text_element).is_equal_to("Hora Inicio") 
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP4_CUR01525")
        time.sleep(5)
    
    @pytest.mark.EP5_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP5_CUR01525(self, driver, username, password):
        """
        IMPORTANT: Los test del EP7 estan contemplados en este test
        Validar que la lista desplegable de selección única, muestres los instructores 
        activos asociados a la ciudad y sede, deben estar organizados alfabéticamente 
        de forma ascendente. El tamaño corresponde al almacenado en el sistema.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        time.sleep(2)
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP5_CUR01525")
        time.sleep(5)

    @pytest.mark.EP6_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP5_CUR01525(self, driver, username, password):
        """
        Validar que el sistema muestre los Filtros de Búsqueda Campo del "Establecimiento", 
        la lista desplegable "Sala" y las opciones "Día", "Mes", "Año" o "Agenda" (agendas ya registradas). 
        Si no hay agendamientos el calendario se debe mostrar vacío. Prototipo A.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_agenda()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        time.sleep(2)
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP6_CUR01525")
        time.sleep(5)

    @pytest.mark.EP8_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP8_CUR01525(self, driver, username, password):
        """
        IMPORTANT: Los test del EP22 estan contemplados en este test

        Validar que al presionar la opción "Aceptar" el sistema valide obligatoriedad 
        y especificaciones en los campos de la ventana "Nueva Agenda".
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_accept_button()
        time.sleep(2)
        text_element=scheduling_page.get_error_message()
        time.sleep(2)
        with check:
            assert_that(text_element).is_equal_to("- Instructor es obligatorio") 
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP8_CUR01525")
        
    
    @pytest.mark.EP16_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP16_CUR01525(self, driver, username, password):
        """
        El sistema debe validar que el Instructor no se encuentre asociado a otro curso en el mismo 
        horario o en el lapso de duración del curso programado y para la fecha seleccionada
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        time.sleep(2)
        scheduling_page.click_event_scheduled()
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP16_CUR01525")
        time.sleep(5)

    @pytest.mark.EP21_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP21_CUR01525(self, driver, username, password):
        """
        Validar que al seleccionar la opción "Cancelar" realice el retorno con la información previamente diligenciada.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_cancel_button()
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP21_CUR01525")
        time.sleep(2)

    @pytest.mark.EP25_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP25_CUR01525(self, driver, username, password):
        """
        Validar que al seleccionar una agenda menor a la del sistema la identifique, generando un mensaje en pantalla “La fecha seleccionada es inferior a la fecha del sistema”.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_back_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        text_element=scheduling_page.get_modal_error_message()
        with check:
            assert_that(text_element).is_equal_to("La fecha seleccionada es inferior a la fecha del sistema")
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP25_CUR01525")
        

    @pytest.mark.EP26_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP26_CUR01525(self, driver, username, password):
        """
        Validar que el sistema identifique que el horario de agendamiento seleccionado, está por fuera del horario de atención 
        generando un mensaje de rechazo en pantalla “El horario seleccionado está fuera del horario de atención configurado en sistema”. 
        Además de permanecer con los campos diligenciados en la misma pantalla.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_no_courser_error_modal() 
        scheduling_page.click_day_option()
        scheduling_page.click_next_option()
        scheduling_page.scroll_top()
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        scheduling_page.click_first_instructor_option()
        scheduling_page.click_accept_button()
        scheduling_page.click_accept_modal_button_twice()
        time.sleep(5)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        time.sleep(3)
        text_element=scheduling_page.get_modal_error_message()
        with check:
            assert_that(text_element).is_equal_to("El horario seleccionado está fuera del horario de atención configurado en sistema") 
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP26_CUR01525")
        time.sleep(3)

    @pytest.mark.EP27_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP27_CUR01525(self, driver, username, password):
        """
        Validar que el sistema identifique que al seleccionar un día que no corresponda a los días de atención del centro de formación 
        se genere un mensaje de rechazo en pantalla “La fecha seleccionada no corresponde con un día de atención del lugar del curso”. 
        Además de permanecer con los campos diligenciados en la misma pantalla.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_no_courser_error_modal() 
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option_until_day_is_sunday()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        time.sleep(2)
        scheduling_page.click_first_instructor_option()
        time.sleep(2)
        scheduling_page.click_accept_button()
        scheduling_page.click_accept_modal_button_twice()
        time.sleep(5)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        time.sleep(3)
        text_element=scheduling_page.get_modal_error_message()
        with check:
            assert_that(text_element).is_equal_to("La fecha seleccionada no corresponde con un día de atención del lugar del curso") 
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP27_CUR01525")
        time.sleep(3)

    @pytest.mark.EP32_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP32_CUR01525(self, driver, username, password):
        """
        Validar que el sistema identifique que el instructor no está Activo en el CIA, OT o CEA generando un mensaje de rechazo en pantalla 
        “El instructor <Nombre Instructor> no se encuentra asociado al <Nombres del CIA, OT o CEA >”, debe retornar y  recuperar los datos ya existente.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_no_courser_error_modal() 
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        time.sleep(2)
        scheduling_page.click_instructor_not_active_option()
        time.sleep(2)
        scheduling_page.click_accept_button()
        scheduling_page.click_accept_modal_button_twice()
        time.sleep(5)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        time.sleep(3)
        text_element=scheduling_page.get_modal_error_message()
        with check:
            assert_that(text_element).is_equal_to("El instructor YPJQ RJGOEC DJOREQ HJGUVQST no se encuentra asociado al CEA ABC DE FORMACIÓN CRA 30") 
        SaveScreenshots.save_screenshot(driver, SCHEDULING_BASE, "EP32_CUR01525")
        time.sleep(3)
    

    
