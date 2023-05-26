class Validators:
    @staticmethod
    def validate_dropdown_menu_elements(dropdown_elements, UI_elements):
        UI_elements_text = set([element.text.rstrip() for element in dropdown_elements])
        return UI_elements_text == UI_elements