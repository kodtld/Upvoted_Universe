from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time

class ScreenShotter:
    def __init__(self, post_url, post_id):
        self.driver = webdriver.Firefox(executable_path='C:/home/kxsalmi/Drivers/geckodriver')
        self.post_url = post_url
        self.post_id = post_id
    
    def titleScreenshot(self):
        self.driver.get(f'{self.post_url}')
        time.sleep(3)

        try:
            element = self.driver.find_element(By.CLASS_NAME, "Post")

        except:
            element = self.driver.find_element(By.ID, f"t3_{self.post_id}")
        
        location = element.location
        size = element.size

        self.driver.save_screenshot(f'/home/kxsalmi/Upvoted_Universe/src/resources/screenshots/{self.post_id}.png')

        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        im = Image.open(f'/home/kxsalmi/Upvoted_Universe/src/resources/screenshots/{self.post_id}.png')
        im = im.crop((int(x), int(y), int(x + width), int(y + height)))
        im.save(f'/home/kxsalmi/Upvoted_Universe/src/resources/screenshots/{self.post_id}.png')

        self.driver.close()

    def commentScreenshot(self):
        pass