import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

class ScreenShotter:
    def __init__(self, post_url, post_id, post_comments):
        self.driver = webdriver.Firefox(executable_path='../drivers/geckodriver')
        self.username = os.getenv('REDDIT_USERNAME')
        self.password = os.getenv('REDDIT_PASSWORD')
        self.post_url = post_url
        self.post_id = post_id
        self.post_comments = post_comments


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

    def close_popup(self):
        time.sleep(1)
        try:
            reject_button = self.driver.find_element(By.XPATH, '//button[text()="Reject non-essential"]')
            reject_button.click()
            close_button = self.driver.find_element(By.XPATH, '//button[@aria-label="Close"]')
            close_button.click()

        except: # pylint: disable=W0702
            pass

    def title_screenshot(self):
        self.driver.get(f'{self.post_url}')
        time.sleep(2)
        self.close_popup()

        try:
            element = self.driver.find_element(By.CLASS_NAME, "Post")

        except: # pylint: disable=W0702
            element = self.driver.find_element(By.ID, f"t3_{self.post_id}")
        
        location = element.location
        size = element.size
        
        new_dir_path = os.path.join(os.getcwd(), 'resources', 'screenshots', self.post_id)
        os.makedirs(new_dir_path, exist_ok=True)


        self.driver.save_screenshot(f'./resources/screenshots/{self.post_id}/title-{self.post_id}.png')

        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        im = Image.open(f'./resources/screenshots/{self.post_id}/title-{self.post_id}.png')
        im = im.crop((int(x), int(y), int(x + width), int(y + height)))
        im.save(f'./resources/screenshots/{self.post_id}/title-{self.post_id}.png')

    def comment_screenshot(self, comment):
        comment_id = comment['id']

        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, f"t1_{comment_id}"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        location = element.location_once_scrolled_into_view
        self.driver.execute_script("window.scrollBy(0, -100);")

        size = element.size
        time.sleep(2)

        self.driver.save_screenshot(f'./resources/screenshots/{self.post_id}/comment-{comment_id}.png')
        
        x = location['x']
        y = location['y'] + 100
        width = size['width']
        height = size['height']
        im = Image.open(f'./resources/screenshots/{self.post_id}/comment-{comment_id}.png')
        im = im.crop((int(x), int(y), int(x + width), int(y + height)))
        im.save(f'./resources/screenshots/{self.post_id}/comment-{comment_id}.png')


    def close_driver(self): 
        self.driver.close()

    def run_screenshot_service(self):
        self.login_reddit()
        self.title_screenshot()
        for comment in self.post_comments:
            self.comment_screenshot(comment)
        self.close_driver()