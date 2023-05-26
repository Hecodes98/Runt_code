from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.actions import Actions
from selenium.common.exceptions import TimeoutException

from config import TIME_SECONDS_UNIT

class AssistantRegistrationPage:
    def __init__(self, driver):
        self.actions = Actions()
        self.driver = driver
        self.accept_modal_button = (By.XPATH, "//button[contains(text(),'Aceptar')]")
        self.document_type_select_input = (By.ID, "mat-select-0")
        self.cc_option = (By.ID, "mat-option-0")
        self.document_number_textbox = (By.ID, "mat-input-0")
        self.consult_button = (By.XPATH, "//span[contains(text(),'Consultar')]")
        self.ticket_number_textbox = (By.ID, "mat-input-19")
        self.ticket_number_textbox_modal_2 = (By.ID, "mat-input-22")
        self.error_message = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/mat-dialog-container[1]/ciasmr-app-registro-infraccion[1]/div[1]/form[1]/div[1]/div[1]/mat-form-field[1]/div[1]/div[2]/div[1]/mat-error[1]")
        self.search_ticket_number = (By.XPATH, "//span[contains(text(),'Buscar comparendo')]")
        self.record_violation = (By.XPATH, "//span[contains(text(),'Registrar Infracción')]")
        self.infraction_error_message = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/mat-dialog-container[1]/ciasmr-app-registro-infraccion[1]/div[1]/form[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[2]/div[1]/mat-error[1]")
        self.modal_error_message = (By.XPATH, "//body[1]/div[3]/div[1]/div[2]")
        self.accept_modal_button_ticket_already_exist = (By.XPATH, "//body[1]/div[3]/div[1]/div[6]/button[1]")
        self.infraction_input = (By.ID, "mat-select-8")
        self.infraction_input_option_1 = (By.XPATH, "//span[contains(text(),'A01 - No transitar por la derecha de la vía.')]")
        self.comparendo_date = (By.ID, "mat-input-20")
        self.entity_input = (By.ID, "mat-select-10")
        self.entity_input_option_1 = (By.XPATH, "//span[contains(text(),'POLCA')]")
        self.transit_authority_input = (By.ID, "mat-input-21")
        self.transit_authority_input_option_1 = (By.XPATH, "//span[contains(text(),'STRIA DE TTOyTTE MEDELLIN')]")
        self.modal_button_infraction_registration = (By.XPATH, "//span[contains(text(),'Aceptar')]")


    def click_accept_modal_button(self):
        try:
            # Esperar a que el campo de usuario esté presente en la página
            modal_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
                EC.presence_of_element_located(self.accept_modal_button)
            )
            modal_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
                EC.element_to_be_clickable(self.accept_modal_button)
            )
            modal_button_element.click()
        except:
            return "There's no error message"


    def click_document_type_select_input(self):
        document_type_select_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.document_type_select_input)
        document_type_select_element.click()
    
    def click_cc_option(self):
        cc_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.cc_option)
        cc_element.click()

    def fill_document_number_textbox(self,document_number):
        document_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.document_number_textbox)
        document_number_element.send_keys(document_number)

    def click_consult_button(self):
        consult_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.consult_button)
        consult_button_element.click()


    def click_search_ticket_number_button(self):
        search_ticket_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.search_ticket_number)
        search_ticket_element.click()


    def click_record_violation_button(self):
        record_violation_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.record_violation)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", record_violation_element)
        record_violation_element.click()

    def fill_ticket_number_textbox(self,ticket_number):
        ticket_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.ticket_number_textbox)
        ticket_number_element.send_keys(ticket_number)

    def fill_ticket_number_textbox_modal_2(self,ticket_number):
        ticket_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.ticket_number_textbox_modal_2)
        ticket_number_element.send_keys(ticket_number)

    def verify_error_message(self):
        try:
            error_message_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.error_message)
            return error_message_element.text
        except TimeoutException:
            return "There's no error message"
        
    def verify_infraction_error_message(self):
        try:
            infraction_error_message_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.infraction_error_message)
            return infraction_error_message_element.text
        except TimeoutException:
            return "There's no error message"
        
    def verify_modal_error_message(self):
        try:
            modal_error_message_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.modal_error_message)
            return modal_error_message_element.text
        except TimeoutException:
            return "There's no error message"
    
    def click_accept_modal_button_ticket_already_exist(self):
        accept_modal_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_modal_button_ticket_already_exist)
        accept_modal_element.click()

    def click_infraction_input(self):
        infraction_input_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.infraction_input)
        infraction_input_element.click()
    
    def click_infraction_input_option_1(self):
        input_option_1_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.infraction_input_option_1)
        input_option_1_element.click()
    
    def send_comparendo_date(self, date):
        input_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.comparendo_date)
        input_date_element.send_keys(date)
    
    def click_entity_input(self):
        entity_input_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.entity_input)
        entity_input_element.click()
    
    def click_entity_input_option_1(self):
        entity_input_option_1_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.entity_input_option_1)
        entity_input_option_1_element.click()
    
    def click_transit_authority_input(self):
        transit_authority_input_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.transit_authority_input)
        transit_authority_input_element.click()

    def click_transit_authority_input_option_1(self):
        transit_authority_input_option_1_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.transit_authority_input_option_1)
        transit_authority_input_option_1_element.click()
    
    def click_modal_button_infraction_registration(self):
        modal_button_infraction_registration_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.modal_button_infraction_registration)
        modal_button_infraction_registration_element.click()

    
    
    

        

