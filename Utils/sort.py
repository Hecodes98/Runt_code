class Sort:
    @staticmethod
    def sort_elements(elements):
        elements = [element.text for element in elements]
        elements.sort() 
        return elements
    
    @staticmethod
    def custom_sort_key(string):
        if string[0].isalpha():
            return (0, string)  # Si el string contiene solo letras
        else:
            return (1, string)  # Si el string contiene caracteres no alfabéticos al inicio


