from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIME_SECONDS_UNIT


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "signInName")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.ID, "next")

    def enter_username(self, username):
        # Esperar a que el campo de usuario esté presente en la página
        username_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.username_textbox)
        )
        username_element.send_keys(username)

    def enter_password(self, password):
        # Esperar a que el campo de contraseña esté presente en la página
        password_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.password_textbox)
        )
        password_element.send_keys(password)

    def click_login(self):
        # Esperar a que el botón de inicio de sesión esté presente y sea visible en la página
        login_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.visibility_of_element_located(self.login_button)
        )
        login_button_element.click()
        
    def fill_inputs_and_click_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        