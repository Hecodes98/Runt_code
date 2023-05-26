from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import TIME_SECONDS_UNIT
from Utils.actions import Actions

import time

class FacilityManagerPage:
    def __init__(self, driver):
        self.actions = Actions()
        self.driver = driver
        self.close_error_button = (By.XPATH, "//button[contains(text(),'Aceptar')]")
        self.new_room_button = (By.XPATH, "//span[contains(text(),'Nueva Sala')]")
        self.schedule_tab = (By.XPATH, "//div[contains(text(),'Horario')]")
        self.name_textbox = (By.CSS_SELECTOR, "input#mat-input-1")
        self.capacity_textbox = (By.CSS_SELECTOR, "input#mat-input-2")
        self.save_button = (By.XPATH, "//span[contains(text(),'Guardar')]")
        self.accept_modal_button = (By.XPATH, "//button[contains(text(),'Aceptar')]")
        self.save_modal_button = (By.XPATH, "//button[contains(text(),'Aceptar')]")
        self.capacity_input_error = (By.ID, "mat-error-3")
        self.first_edit_button = (By.XPATH, "//tbody/tr[1]/td[3]/button[1]/span[1]")

        #Schedule

        self.new_schedule_button = (By.XPATH, "//span[contains(text(),'Nuevo Horario')]")
        self.diary_radio_button = (By.ID, "mat-radio-2")
        self.weekly_radio_button = (By.ID, "mat-radio-3")
        self.day_select_input = (By.ID, "mat-select-0")
        self.monday_option = (By.XPATH, "//span[contains(text(),'Lunes')]")
        self.sunday_option = (By.XPATH, "//span[contains(text(),'Domingos y Festivos')]")
        self.init_time_select_input = (By.XPATH, "//body/div[1]/div[2]/div[1]/mat-dialog-container[1]/ciasmr-horario-modal[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[2]")
        self.init_time_option_1 = (By.XPATH, "//span[contains(text(),'01')]")
        self.init_time_option_2 = (By.XPATH, "//mat-option[@id='mat-option-5']")
        self.init_minute_select_input = (By.ID, "mat-select-4")
        self.init_minute_option_1 = (By.XPATH, "//span[contains(text(),'00')]")
        self.init_meridian_select_input = (By.ID, "mat-select-6")
        self.init_meridian_option_1 = (By.XPATH, "//span[contains(text(),'PM')]")
        self.end_time_select_input = (By.ID, "mat-select-8")
        self.end_time_option_1 = (By.XPATH, "//span[contains(text(),'03')]") #TODO VALIDAR OTRA FORMA DE ENCONTRAR LOS SUB ELEMENTOS, YA QUE ESAS LISTAS NO SON LISTAS SELECT Y SE DEBEN TRATAR COMO ELEMENTOS NORMALES DE LA PAGINA WEB 
        self.end_minute_select_input = (By.ID, "mat-select-10")
        self.end_minute_option_1 = (By.XPATH, "//span[contains(text(),'05')]") #TODO VALIDAR OTRA FORMA DE ENCONTRAR LOS SUB ELEMENTOS, YA QUE ESAS LISTAS NO SON LISTAS SELECT Y SE DEBEN TRATAR COMO ELEMENTOS NORMALES DE LA PAGINA WEB
        self.end_meridian_select_input = (By.ID, "mat-select-12")
        self.end_meridian_option_1 = (By.XPATH, "//body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]")#TODO VALIDAR OTRA FORMA DE ENCONTRAR LOS SUB ELEMENTOS, YA QUE ESAS LISTAS NO SON LISTAS SELECT Y SE DEBEN TRATAR COMO ELEMENTOS NORMALES DE LA PAGINA WEB

    

    def click_accept_button_for_close_error_modal(self):
        try:
            close_modal = self.actions.element_to_be_clickable(driver=self.driver, element=self.close_error_button)
            close_modal.click()
        except TimeoutException:
            return None

    def click_new_room_button(self):
        new_room_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.new_room_button)
        new_room_element.click()

    def click_schedule_tab(self):
        schedule_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.schedule_tab)
        schedule_element.click()

    def click_new_schedule_button(self):
        new_schedule_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.new_schedule_button)
        new_schedule_element.click()
    
    def fill_name_textbox(self, name):
        name_textbox_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.name_textbox)
        name_textbox_element.send_keys(name)

    def fill_capacity_textbox(self, capacity):
        capacity_textbox_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.capacity_textbox)
        capacity_textbox_element.send_keys(capacity)

    def click_save_button(self):
        save_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.save_button)
        save_button_element.click()
    
    def click_accept_modal_button_twice(self):
        accept_modal_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_modal_button)
        accept_modal_button_element.click()
        accept_modal_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_modal_button)
        accept_modal_button_element.click()

    def click_save_modal_button(self):
        save_modal_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.save_modal_button)
        save_modal_element.click()

    def get_capacity_error_message(self):
        try:
            self.actions.element_to_be_clickable(driver=self.driver, element=self.capacity_input_error)
            return True
        except TimeoutException:
            return False
        
    def click_first_edit_button(self):
        first_edit_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.first_edit_button)
        first_edit_element.click()

    #Schedule

    def click_diary_radio_button(self):
        diary_radio_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.diary_radio_button)
        diary_radio_element.click()
    
    def click_weekly_radio_button(self):
        weekly_radio_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.weekly_radio_button)
        )
        weekly_radio_element.click()

    def click_day_select_input(self):
        day_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.day_select_input)
        )
        day_select_element.click()

    def click_monday_option(self):
        monday_option_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.monday_option)
        )
        monday_option_element.click()
    
    def click_sunday_option(self):
        sunday_option_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.sunday_option)
        )
        sunday_option_element.click()

    def click_init_time_select_input(self):
        init_time_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.init_time_select_input)
        )
        init_time_select_element.click()

    def click_init_time_option_1(self):
        init_time_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.init_time_option_1)
        )
        init_time_element.click()

    def click_init_time_option_2(self):
        init_time_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.init_time_option_2)
        )
        init_time_element.click()

    def click_init_minute_select_input(self):
        init_minute_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.init_minute_select_input)
        )
        init_minute_select_element.click()

    def click_init_minute_option_1(self):
        init_minute_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.init_minute_option_1)
        )
        init_minute_element.click()

    def click_meridian_select_input(self):
        meridian_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.init_meridian_select_input)
        )
        meridian_select_element.click()

    def click_meridian_option_1(self):
        meridian_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.init_meridian_option_1)
        )
        meridian_select_element.click()

    #########

    def click_end_time_select_input(self):
        end_time_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.end_time_select_input)
        )
        end_time_select_element.click()

    def click_end_time_option_1(self):
        end_time_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.end_time_option_1)
        )
        end_time_element.click()

    def click_end_minute_select_input(self):
        end_minute_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.end_minute_select_input)
        )
        end_minute_select_element.click()

    def click_end_minute_option_1(self):
        end_minute_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.end_minute_option_1)
        )
        end_minute_element.click()

    def click_end_meridian_select_input(self):
        meridian_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.end_meridian_select_input)
        )
        meridian_select_element.click()

    def click_end_meridian_option_1(self):
        meridian_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.end_meridian_option_1)
        )
        meridian_select_element.click()