from pywinauto.application import Application
import time

class SignatureProcess:
    def __init__(self):
        self.app = None
        self.top_window = None
        self.main_window=None

    def setup_app(self, title):
        self.app = Application().connect(title=title)
        self.top_window = self.app.window(title_re=title, visible_only=False)
        self.top_window.restore().set_focus()
        self.main_window = self.app.top_window()

    def signature_process(self):
        self.setup_app(title="Certificados")
        x_click_signature = 55
        y_click_signature = 100
        x_click_accept = 220
        y_click_accept = 500        
        self.top_window.click_input(coords=(x_click_signature,y_click_signature))
        self.top_window.click_input(coords=(x_click_accept,y_click_accept))
        time.sleep(5)
        self.setup_app(title="Se están firmando datos con su clave privada de intercambio")
        x_click_signature = 250
        y_click_signature = 150
        x_click_accept = 150
        y_click_accept = 250
        self.top_window.click_input(coords=(x_click_signature,y_click_signature))
        self.top_window.type_keys("123456789")
        self.top_window.click_input(coords=(x_click_accept,y_click_accept))
