import os

class SaveScreenshots:
    @staticmethod
    def save_screenshot(driver,path_base,us_id):
        if not os.path.exists(f"{path_base}{us_id}/"):
            os.makedirs(f"{path_base}{us_id}/")    
        print(f"{path_base}{us_id}/{us_id}.png")
        driver.save_screenshot(f"{path_base}{us_id}/{us_id}.png")
