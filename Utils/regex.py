import re

class ReGex:
    @staticmethod
    def date_validation_format(date):
        pattern = r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0?[1-9]|1[0-2])/\d{4}$"
        return re.match(pattern, date) is not None