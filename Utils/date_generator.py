from datetime import date, timedelta
from config import DAYS_AGO

class DateGenerator:
    @staticmethod
    def get_today_formatted_date():
        today_date = date.today()
        return today_date.strftime('%Y-%m-%d')
    
    @staticmethod
    def get_date_minus_parameter_days():
        print((date.today() - timedelta(days=DAYS_AGO)).strftime("%Y-%m-%d"))
        return (date.today() - timedelta(days=DAYS_AGO)).strftime("%Y-%m-%d")

    @staticmethod
    def get_tomorrow_date():
        today = date.today()
        tomorrow = today + timedelta(days=1)
        formatted_date = tomorrow.strftime("%d/%m/%y")
        return formatted_date