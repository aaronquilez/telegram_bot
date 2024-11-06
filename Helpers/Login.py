
from Constants.Env import LOGIN_URL

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.file_detector import LocalFileDetector


class Login:
   

    def login_to_webpage(username: str, password: str, day: str) -> str:

        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--windows-size=0,0")
        
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444', options=chrome_options)
        #driver = webdriver.Chrome(options=chrome_options)

        driver.get(LOGIN_URL)

        time.sleep(5)
        driver.find_element(By.ID, 'data.email').send_keys(username)
        driver.find_element(By.ID, 'data.password').send_keys(password)

        driver.find_element(By.CLASS_NAME, 'fi-btn').click()
        time.sleep(3)
        try: 
            elements = driver.find_elements(By.CLASS_NAME, 'ring-primary-600')
            dies = {}
            detall = []

            for e in elements:
                detall = e.text.splitlines()
                key = detall.pop(0)
                dies[key] = detall

            driver.quit()
            return (dies[day])
        except:
            return ("No s'ha registrat correctament")

