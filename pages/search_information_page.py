from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from Utils.actions import Actions
from Utils.validators import Validators
from Utils.sort import Sort
from Utils.regex import ReGex
from config import TIME_SECONDS_UNIT



class SearchInformationPage:
    def __init__(self, driver):
        self.actions = Actions()
        self.validators = Validators()
        self.driver = driver
        self.document_select_input = (By.CSS_SELECTOR, "#mat-select-0[formcontrolname='tipoDocumentoId']")
        self.panel_document_select_options = (By.CSS_SELECTOR, "#mat-select-0-panel mat-option")
        self.cc_option = (By.ID, "mat-option-3")
        self.document_number_textbox = (By.CSS_SELECTOR, "input[formcontrolname='numeroDocumento']")
        self.ticket_initial_date = (By.CSS_SELECTOR, "input[formcontrolname='fechaInicio']")
        self.ticket_final_date = (By.CSS_SELECTOR, "input[formcontrolname='fechaTerminacion']")
        self.ticket_number_textbox = (By.CSS_SELECTOR, "input[formcontrolname='numeroComparendo']")
        self.infraction_number = (By.CSS_SELECTOR, "input[formcontrolname='infraccionNumero']")
        self.ticket_number_error = (By.ID, "mat-error-0")
        self.search_button = (By.XPATH, "//span[contains(text(),'Buscar')]")
        self.modal_message_error = (By.ID, "swal2-html-container")
        self.clean_button = (By.XPATH, "//span[contains(text(),'Limpiar')]")
        self.edit_buttons = (By.XPATH, "//span[contains(text(),'Editar')]")
        self.limit_edit_modal_button = (By.XPATH, "//body[1]/div[3]/div[1]/div[6]/button[1]")
        self.calendar_date_month = (By.ID, "mat-calendar-button-0")
        self.init_date_icon = (By.CSS_SELECTOR, "mat-datepicker-toggle[data-mat-calendar='mat-datepicker-0']")
        self.end_date_icon = (By.CSS_SELECTOR, "mat-datepicker-toggle[data-mat-calendar='mat-datepicker-1']")
        self.back_month_button = (By.CSS_SELECTOR, "button[aria-label='Previous month']")
        self.today_date = (By.CSS_SELECTOR, "div.mat-calendar-body-today")
        self.exact_date = (By.CSS_SELECTOR, "button[aria-label='18 de abril de 2023']")
        self.save_edit_button = (By.XPATH, "//body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/ciasmr-app-editar-infraccion[1]/div[2]/button[2]/span[1]")
        self.edit_modal_dropdown_ticket = (By.ID, "mat-select-2")
        self.edit_modal_dropdown_elements = (By.CSS_SELECTOR, "span.mat-option-text")
        self.ticket_date = (By.ID, "mat-input-5")
        self.entity_input = (By.ID, "mat-select-4")
        self.ticket_number_from_table = (By.CSS_SELECTOR, "td.mat-column-numeroComparendo")
        self.accept_modal_button = (By.XPATH, "//body[1]/div[3]/div[1]/div[6]/button[1]")


    def click_select_input_type_document_cc(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_select_input)
        )
        # Esperar hasta que el elemento sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.visibility_of_element_located(self.document_select_input)
        )
        element.click()

        cc_option_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.cc_option)
        )

        cc_option_element.click()

    def click_select_input(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_select_input)
        )
        # Esperar hasta que el elemento sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.visibility_of_element_located(self.document_select_input)
        )
        element.click()


    def get_all_dropdown_options(self, UI_elements):
        dropdown_options = self.actions.presence_of_all_elements_located(driver=self.driver, element=self.panel_document_select_options)
        return self.validators.validate_dropdown_menu_elements(dropdown_options, UI_elements)

    def send_document_number(self, document_number):
        input_document_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.document_number_textbox)
        input_document_number_element.send_keys(document_number)

    def send_ticket_initial_date(self, ticket_initial_date):
        initial_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.ticket_initial_date)
        initial_date_element.send_keys(ticket_initial_date)

    def send_ticket_final_date(self, ticket_final_date):
        final_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.ticket_final_date)
        final_date_element.send_keys(ticket_final_date)
    
    def send_ticket_number(self, ticket_number):
        ticket_number_textbox_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.ticket_number_textbox)
        ticket_number_textbox_element.send_keys(ticket_number)
    
    def click_search_button(self):
        search_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.search_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", search_button_element)
        search_button_element.click()

    def click_clean_button(self):
        clean_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.clean_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", clean_button_element)
        clean_button_element.click()

    def get_ticket_number_error(self):
        try:
            ticket_number_error_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.ticket_number_error)
            return ticket_number_error_element.text
        except TimeoutException:
            return "There's no error message"
    
    def get_modal_message_error(self):
        try:
            modal_message_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.modal_message_error)
            return modal_message_element.text
        except TimeoutException:
            return "There's no error message"
    
    def click_edit_until_edit_works(self):
        edit_buttons_elements = self.actions.presence_of_all_elements_located(driver=self.driver, element=self.edit_buttons)
        self.driver.execute_script("arguments[0].scrollIntoView();", edit_buttons_elements[0])
        for edit_button_element in edit_buttons_elements:
            edit_button_element.click()
            try:
                limit_edit_modal_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.limit_edit_modal_button)
                )
                limit_edit_modal_element.click()
            except TimeoutException:
                return "There's no error message"
            
    def click_init_date(self):
        init_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.init_date_icon)
        init_date_element.click()

    def click_end_date(self):
        end_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.end_date_icon)
        end_date_element.click()
    
    def click_today_date(self):
        today_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.today_date)
        today_date_element.click()

    def click_today_date(self):
        today_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.today_date)
        today_date_element.click()
    
    def select_april_date(self):
        calendar_date_month_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.calendar_date_month)
        back_month_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.back_month_button)
        while(calendar_date_month_element.text != "ABR DE 2023"):
            back_month_button_element.click()
        exact_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.exact_date)
        exact_date_element.click()

    def click_infraction_number_input(self):
        infraction_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.infraction_number)
        infraction_number_element.click()

    def delete_default_infraction_data(self):
        infraction_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.infraction_number)
        infraction_number_element.click()
        infraction_number_element.send_keys(Keys.CONTROL, 'a')
        infraction_number_element.send_keys(Keys.DELETE)

    def send_infraction_data(self, ticket_number):
        infraction_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.infraction_number)
        infraction_number_element.send_keys(ticket_number)

    def get_infraction_data(self):
        infraction_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.infraction_number)
        return infraction_number_element.get_attribute('value').lstrip().rstrip()
    
    def click_save_edit_button(self):
        save_edit_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.save_edit_button)
        save_edit_button_element.click()

    def click_edit_modal_dropdown_ticket(self):
        edit_modal_dropdown_ticket_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.edit_modal_dropdown_ticket)
        edit_modal_dropdown_ticket_element.click()
    
    def validate_sort_edit_modal_dropdown_elements(self):
        edit_modal_dropdown_elements_elements = self.actions.presence_of_all_elements_located(driver=self.driver, element=self.edit_modal_dropdown_elements)
        edit_modal_dropdown_elements_elements_text = [element.text.lstrip().rstrip() for element in edit_modal_dropdown_elements_elements]
        sorted_elements_text = sorted(edit_modal_dropdown_elements_elements_text, key=Sort.custom_sort_key)
        return edit_modal_dropdown_elements_elements_text == sorted_elements_text
    
    def validate_ticket_date(self):
        tickets_date_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.ticket_date)
        first_date = tickets_date_element.get_attribute('value').lstrip().rstrip()
        print(first_date)
        return ReGex.date_validation_format(first_date)
    
    def click_entity_input(self):
        entity_input_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.entity_input)
        entity_input_element.click()
        
    def click_accept_modal_button_twice(self):
        accept_modal_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_modal_button)
        accept_modal_button_element.click()
        accept_modal_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_modal_button)
        accept_modal_button_element.click()
        
    
    
    



    