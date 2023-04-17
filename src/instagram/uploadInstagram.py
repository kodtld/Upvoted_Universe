import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()

class InstagramUploader:
    def __init__(self, post_id, post_author):
        self.post_id = post_id
        self.driver = webdriver.Firefox(executable_path='C:/home/kxsalmi/Drivers/geckodriver')
        self.username = os.getenv('INSTAGRAM_USERNAME')
        self.password = os.getenv('INSTAGRAM_PASSWORD')
        hashtags = ("#upvoteduniverse #tiktok #askreddit #askredditanswers #askredditquestions #askredditstories "
                    "#askredditthread #askredditmen #askredditpost #askredditafterdark "
                    "#askredditquestion #askredditjoke #askredditdaily #askredditfunny "
                    "#askreddittopposts #askredditmemes #relatable #dumb #memepages "
                    "#reddit #relatablememes #storytelling #interesting #dailymemez "
                    "#textpostfunny #edgyhumour #genzhumor #textfails #redditcrew #redditmemes ")
        
        self.caption = f'⬆️ By reddit user: @{post_author} \nFollow @upvoteduniverse for daily reddit posts!\n\n\n\n\n{hashtags}'

    def login_instagram(self):
        self.driver.get('https://www.instagram.com/accounts/onetap/?next=%2F')
        time.sleep(2)

        cookies_button = self.driver.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]')
        cookies_button.click()
        time.sleep(2)

        username_field = self.driver.find_element(By.NAME, 'username')
        username_field.send_keys(self.username)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)

        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        time.sleep(2)
   


    def upload_video(self):
        try:
            not_now_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not Now"]')))
            not_now_button.click()
        except:
            pass

        create_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[text()="Create"]')))
        create_button.click()

        select_from_computer_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Select From Computer"]')))
        select_from_computer_button.click()

        file_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
        file_input.send_keys(f'/home/kxsalmi/Upvoted_Universe/src/resources/final_videos/{self.post_id}_final.mp4')

        ok_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="OK"]')))
        ok_button.click()

        aspect_ratio_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '_acan._acao._acas._aj1-')))
        aspect_ratio_button.click()

        original_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Original"]')))
        original_button.click()

        next_button_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Next"]')))
        next_button_1.click()

        next_button_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Next"]')))
        next_button_2.click()

        caption_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Write a caption..."]')))
        for letter in self.caption:
            caption_input.send_keys(letter)

        time.sleep(2)

        share_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Share"]')))
        share_button.click()
        
        try_count = 0
        
        while True:
            try:
                # Check if the "Reel shared" div is present
                WebDriverWait(self.driver, 90).until(
                    EC.presence_of_element_located((By.XPATH, '//div[text()="Reel shared"]'))
                )
            
                os.remove(f'/home/kxsalmi/Upvoted_Universe/src/resources/final_videos/{self.post_id}_final.mp4')
                break
            
            except:
                try_again_button = self.driver.find_element(By.XPATH, '//button[text()="Try Again"]')
                if try_again_button.is_displayed():
                    try_again_button.click()
                    try_count +=1
                    print(f"Trycount: {try_count}/5")
                    time.sleep(2)
                    if try_count > 5:
                        break
                    continue

                else:
                    time.sleep(2)
                    continue
            
    def close_driver(self): 
        self.driver.close()

    def run_screenshot_service(self):
        self.login_instagram()
        self.upload_video()
        self.close_driver()

# if __name__ == "__main__":
#     i = InstagramUploader("12ocf1t", "Redditboy493")
#     i.run_screenshot_service()
