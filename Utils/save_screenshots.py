import os

class SaveScreenshots:
    @staticmethod
    def save_screenshot(driver,path_base,us_id):
        if not os.path.exists(f"{path_base}/"):
            os.makedirs(f"{path_base}/")    
        print(f"{path_base}/{us_id}.png")
        driver.save_screenshot(f"{path_base}/{us_id}.png")
