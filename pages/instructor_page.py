from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIME_SECONDS_UNIT


class InstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.document_type_select_input = (By.ID, "mat-select-0")
        self.cc_option = (By.ID, "mat-option-0")
        self.document_number_textbox = (By.ID, "mat-input-0")

        

    def click_document_type_select_input(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        document_type_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.document_type_select_input)
        )
        document_type_select_element.click()

    def click_cc_option(self):
        cc_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.cc_option)
        )
        cc_element.click()

    def fill_document_type_textbox(self, document_number):
        document_number_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_number_textbox)
        )
        document_number_element.send_keys(document_number)