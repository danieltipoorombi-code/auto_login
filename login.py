import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

def  StartBot(username, password, url):
    path = "C:\\Users\\j\\Downloads\\ChromeSetup.exe"

    #create a service object
    service = Service(path)

    #set up chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # run in headless mode

    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("Opening the browser...")
    driver.get(url)

    print("Waiting for the page to load...")
    time.sleep(5)  # wait for the page to load

    print("Entering login...")
    driver.find_element(By.NAME, "login").send_keys(username)

    print("Entering password...")
    driver.find_element(By.NAME, "password").send_keys(password)

    print("Clicking the login button...")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    print("Login processing...")
    driver.implicitly_wait(5)  # wait for the login to process

    driver.quit()
    if __name__ == "__main__":
      username = input("Danny ")
      password = input("12334 ")

#url in pageof the log
      url = "https://github.com/login"
#call the function
      StartBot(username, password, url)
