PROMISED_DOWN=150
PROMISED_UP=10
TWITTER_EMAIL="anirudhpabbaraju1103@gmail.com"
TWITTER_PASSWORD="anirudh@1103"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

class InternerSpeedTwitterBot:
    def __init__(self):
        self.down=0
        self.up=0
        self.driver=webdriver.Chrome(options=chrome_options)
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        
        
        time.sleep(3)
        go=self.driver.find_element(By.CSS_SELECTOR,value="div.start-button a")
        go.click()
        
       
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        
        print("Up"+self.up)
        print("Down" + self.down)
        self.driver.quit()
        
    def sign_in_process(self):
        time.sleep(3)
        
        sign_in=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span')
        sign_in.click()
        
        time.sleep(3)
        
        time.sleep(3)
        email=self.driver.find_element(By.CSS_SELECTOR,value='input')
        email.send_keys(TWITTER_EMAIL)
        
        next=self.driver.find_elements(By.CSS_SELECTOR,value='button')[2]
        next.click()
        
        time.sleep(3)
        user_name=self.driver.find_element(By.CSS_SELECTOR,value="input")
        user_name.send_keys("AnirudhPab94763")
        
        time.sleep(3)
        log_in=self.driver.find_element(By.CSS_SELECTOR,value='button')
        log_in.click()
        


    def tweet_at_provider(self):
        
        self.driver.get("https://x.com/?lang=en")
        self.sign_in_process()
        # self.sign_in_process()
        
        password=self.driver.find_element(By.CSS_SELECTOR,value='input')
        password.send_keys(TWITTER_PASSWORD)
        
        time.sleep(3)
        log_in=self.driver.find_element(By.CSS_SELECTOR,value="button")
        log_in.click()
        
        time.sleep(3)
        post_msg=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post_msg.send_keys(f"Hey internet provider my upload speed is {self.up} MBPS and download speed is {self.down} MBPS")
        
        time.sleep(3)
        post=self.driver.find_element(By.CSS_SELECTOR,value="button")
        post.click()

bot=InternerSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()

