from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.actions import Actions
from selenium.common.exceptions import TimeoutException
from Utils.sort import Sort

from config import TIME_SECONDS_UNIT

class SchedulingPage:
    def __init__(self, driver):
        self.actions = Actions()
        self.driver = driver
        self.room_select_input = (By.XPATH, "//mat-select[@id='mat-select-0']")
        self.room_one_option = (By.CSS_SELECTOR, "span.mat-option-text")
        self.instructor_not_active = (By.XPATH, "//span[contains(text(),'YPJQ RJGOEC DJOREQ HJGUVQST')]")
        self.day_option_button = (By.XPATH, "//button[contains(text(),'Día')]")
        self.agenda = (By.XPATH, "//button[contains(text(),'Agenda')]")
        self.next_option_button = (By.XPATH, "//button[contains(text(),'>')]")
        self.back_option_button = (By.XPATH, "//button[contains(text(),'<')]")
        self.time_selection_option = (By.XPATH, "//tbody/tr[7]/td[2]")
        self.instructor_select_input = (By.CSS_SELECTOR, "mat-select[formcontrolname='instructor']")
        self.first_instructor_option = (By.XPATH, "//span[contains(text(),'BEOTWQJ')]")
        self.accept_button = (By.XPATH, "//span[contains(text(),'Aceptar')]")
        self.accept_modal_button = (By.XPATH, "//body[1]/div[3]/div[1]/div[6]/button[1]")
        self.cancel_button = (By.XPATH, "//span[contains(text(),'Cancelar')]")
        self.init_time = (By.XPATH, "//mat-label[contains(text(),'Hora Inicio')]")
        self.error_message = (By.ID, "mat-error-1")
        self.scheduled_events = (By.CSS_SELECTOR, "div a.fc-event")
        self.rooms_list = (By.CSS_SELECTOR, "span.mat-option-text")
        self.modal_previous_date_modal_error = (By.ID, "swal2-html-container")
        self.week_day = (By.XPATH, "//body[1]/host-runt-root[1]/app-layout[1]/app-theme-runt2[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/div[1]/ng-component[1]/div[2]/div[2]/ciasmr-calendar[1]/full-calendar[1]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[1]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/a[1]")
        self.no_courses_error_modal = (By.XPATH, "//body[1]/div[3]/div[1]/div[6]/button[1]")

    def click_room_select_input(self):
        select_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.room_select_input)
        select_element.click()
    
    def click_room_one_option(self):
        room_one_elements = self.actions.presence_of_all_elements_located(driver=self.driver, element=self.room_one_option)
        room_one_elements[0].click()

    def click_instructor_not_active_option(self):
        instructor_not_active_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.instructor_not_active)
        self.driver.execute_script("arguments[0].scrollIntoView();", instructor_not_active_element)
        instructor_not_active_element.click()
    
    def click_day_option(self):
        day_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.day_option_button)
        day_button_element.click()

    def click_next_option(self):
        next_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.next_option_button)
        next_element.click()
    
    def click_next_option_until_day_is_sunday(self):
        next_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.next_option_button)
        while self.actions.element_to_be_clickable(driver=self.driver, element=self.week_day).text != 'domingo':
            next_element.click()
    
    def click_back_option(self):
        back_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.back_option_button)
        back_element.click()

    def scroll_top(self):
        reference_element_to_scroll = self.actions.element_to_be_clickable(driver=self.driver, element=self.room_select_input)
        self.driver.execute_script("arguments[0].scrollIntoView();", reference_element_to_scroll)

    def click_record_violation_button(self):
        time_selection_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.time_selection_option)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", time_selection_element)
        time_selection_element.click()

    def click_instruction_input_option(self):
        instructor_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.instructor_select_input)
        instructor_element.click()
        
    
    def click_first_instructor_option(self):
        first_instructor_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.first_instructor_option)
        first_instructor_element.click()
    
    def click_accept_button(self):
        accept_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_button)
        accept_button_element.click()
    
    def click_cancel_button(self):
        cancel_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.cancel_button)
        cancel_button_element.click()

    def click_agenda(self):
        agenda_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.agenda)
        agenda_element.click()

    def validate_inputs_appears(self):
        time_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.init_time)
        return time_element.text
    
    def get_error_message(self):
        error_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.error_message)
        return error_element.text
    
    def click_event_scheduled(self):
        scheduled_element = self.actions.get_random_element_from_a_list_of_elemenets(driver=self.driver, element=self.scheduled_events)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", scheduled_element)
        scheduled_element.click()

    def validate_order_of_rooms_list(self):
        rooms_list = self.actions.get_a_list_of_elemenets(driver=self.driver, element=self.rooms_list)
        sorted_rooms = Sort.sort_elements(rooms_list) 
        rooms_list = [room.text for room in rooms_list]
        return rooms_list == sorted_rooms
    
    def get_modal_error_message(self):
        modal_error_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.modal_previous_date_modal_error)
        return modal_error_element.text
    
    def click_accept_modal_button_twice(self):
        accept_modal_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_modal_button)
        accept_modal_button_element.click()
        accept_modal_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_modal_button)
        accept_modal_button_element.click()

    def click_no_courser_error_modal(self):
        modal_error_element = self.actions.possible_element_to_be_clickable(driver=self.driver, element=self.no_courses_error_modal, time=15)
        if modal_error_element:
            modal_error_element.click()
        else: 
            return
