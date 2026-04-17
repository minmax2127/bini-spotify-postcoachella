from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper
import time
import random

from bs4 import BeautifulSoup

cookie_pkls = ["cookies.pkl", "cookies_2.pkl"]
def login_using_cookies(base_url = "https://charts.spotify.com/charts/overview/global"):
    ''' use pre-saved cookies to log into a session '''
    try:
        # get random cookie
        chosen = random.choice(cookie_pkls)
        cookies = helper.load_pkl_data(f"cookies/cookies.pkl")

        driver = webdriver.Chrome()
        driver.get(base_url) # Load domain
        try:
            # Inject the cookie
            for cookie in cookies:
                driver.execute_cdp_cmd("Network.enable", {})
                driver.execute_cdp_cmd("Network.setCookie", cookie)
            return driver
        except Exception as e:
            print("Error logging in using cookie", e)
        
    except Exception as e:
        print(f"Error : {e}")
        print("Error logging in using cookie", e)


def get_page_soup(url, driver):
    ''' Get the soup objct of the entire page'''
    driver.get(url)
    try:
        # wait until the songs table is visible in the site
        _ = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        #print(_.text)
        return BeautifulSoup(driver.page_source, "html.parser")
    except Exception as e:
        print(f"Error: {e}")    

    finally:
        driver.quit()