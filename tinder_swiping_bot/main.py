from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")



time.sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

time.sleep(2)
more_button = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button')
more_button.click()



time.sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
fb_login.click()

base_window=driver.window_handles[0]
fb_login_window=driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.NAME,value="email")
password = driver.find_element(By.NAME, value='pass')
time.sleep(2)
email.send_keys("anirudhpabbaraju1103@gmail.com")
password.send_keys("anirudh@1103")
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)


time.sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()



for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()