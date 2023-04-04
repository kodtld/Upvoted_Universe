import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

class ScreenShotter:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='C:/home/kxsalmi/Drivers/geckodriver')
        self.username = os.getenv('REDDIT_USERNAME')
        self.password = os.getenv('REDDIT_PASSWORD')

    def login_reddit(self):
        self.driver.get('https://www.reddit.com/login/')
        time.sleep(2)

        username_field = self.driver.find_element(By.ID, 'loginUsername')
        username_field.send_keys(self.username)

        password_field = self.driver.find_element(By.ID, 'loginPassword')
        password_field.send_keys(self.password)

        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        time.sleep(2)

    def title_screenshot(self, post_url, post_id):
        self.driver.get(f'{post_url}')
        time.sleep(2)
        
        close_button = self.driver.find_element(By.XPATH, '//button[@aria-label="Close"]')
        close_button.click()

        try:
            element = self.driver.find_element(By.CLASS_NAME, "Post")

        except:
            element = self.driver.find_element(By.ID, f"t3_{post_id}")
        
        location = element.location
        size = element.size

        self.driver.save_screenshot(f'/home/kxsalmi/Upvoted_Universe/src/resources/screenshots/{post_id}.png')

        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        im = Image.open(f'/home/kxsalmi/Upvoted_Universe/src/resources/screenshots/{post_id}.png')
        im = im.crop((int(x), int(y), int(x + width), int(y + height)))
        im.save(f'/home/kxsalmi/Upvoted_Universe/src/resources/screenshots/{post_id}.png')

    def comment_screenshot(self):
        pass

    def close_driver(self):
        self.driver.close()
