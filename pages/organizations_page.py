from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utils.date_generator import DateGenerator
from Utils.actions import Actions

from config import TIME_SECONDS_UNIT

import time

class OrganizationsPage:
    def __init__(self, driver):
        self.actions = Actions()
        self.driver = driver
        self.organization_type_input = (By.ID,"mat-select-0")
        self.organization_CEA_type = (By.ID, "mat-option-2")
        self.document_type_input = (By.ID, "mat-select-2")
        self.document_type_cc = (By.ID, "mat-option-4")
        self.document_type_nit = (By.ID, "mat-option-5")
        self.document_number_textbox = (By.ID, "mat-input-1")
        self.commercial_registration_number_textbox = (By.ID, "mat-input-2")
        self.search_button = (By.XPATH, "//span[contains(text(),'Buscar')]")
        self.accept_modal_button = (By.XPATH, "//button[contains(text(),'Aceptar')]")
        self.clean_button = (By.XPATH, "//span[contains(text(),'Limpiar')]")


    def click_organization_type_input(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.organization_type_input)
        )
        # Esperar hasta que el elemento sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.visibility_of_element_located(self.organization_type_input)
        )
        element.click()

        organization_CEA_type_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.organization_CEA_type)
        organization_CEA_type_element.click()
        time.sleep(5)

    def click_document_type_and_select_cc(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        element = self.actions.element_to_be_clickable(driver=self.driver, element=self.document_type_input)
        # Esperar hasta que el elemento sea visible en la página
        element.click()
        cc_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.document_type_cc)
        cc_element.click()
        time.sleep(5) #TODO: Helper momentaneo, buscar una solución más efectiva para el tiempo de desaparición del input select dropdown

    def click_document_type_and_select_nit(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        element = self.actions.element_to_be_clickable(driver=self.driver, element=self.document_type_input)
        # Esperar hasta que el elemento sea visible en la página
        element.click()
        nit_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.document_type_nit)
        nit_element.click()
        time.sleep(5) #TODO: Helper momentaneo, buscar una solución más efectiva para el tiempo de desaparición del input select dropdown

    def get_today_day_input(self):
        try:
            self.today_formatted_date = (By.CSS_SELECTOR, f"input[max='{DateGenerator.get_date_minus_parameter_days()}']")
            element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
                EC.presence_of_element_located(self.today_formatted_date)
            )
            return element.get_attribute('max')
        except TimeoutException:
            return None

    def send_document_number(self, document_number):
        document_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.document_number_textbox)
        document_number_element.send_keys(document_number)

    def send_commercial_registration_number(self, commercial_registration_number):
        commercial_registration_number_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.commercial_registration_number_textbox)
        commercial_registration_number_element.send_keys(commercial_registration_number)
    
    def click_search_button(self):
        search_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.search_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_button_element)
        search_button_element.click()
    
    def click_clean_button(self):
        clean_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.clean_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", clean_button_element)
        clean_button_element.click()

    def click_accept_button(self):
        accept_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.search_button)
        accept_button_element.click()