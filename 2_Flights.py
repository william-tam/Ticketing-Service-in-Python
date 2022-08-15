# This program scraps Google Flights and places them in the CLI. 
# The output for the CLI includes flight numbers, prices, and destinations. ie.     ---flights number-----prices------destinations-----
from cgitb import text
from re import search
import time
# the selenium and webdriver libraries that interacts with webpages.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# PATH has been automated by chromDriverManager service.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Initialize a 5 second wait time for the system.
wait = WebDriverWait(driver,5)

# Google flights url, MAKE SURE IT EXISTS.
url = 'https://www.google.com/travel/flights/search?tfs=CBwQAhopagwIAhIIL20vMGpicnISCjIwMjItMDQtMDlyDQgCEgkvbS8wMl8yODYaKWoNCAISCS9tLzAyXzI4NhIKMjAyMi0wNC0xMHIMCAISCC9tLzBqYnJycAGCAQsI____________AUABSAGYAQE'

# Prevent the DevTools solution message from popping up by using Options functionality.
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Open the chrome url page.
# driver = webdriver.Chrome(executable_path=url, options=options)
driver.get(url)

# Modify the page first so the webscraper can get scraping. 
driver.maximize_window()

# Searching for elements in the HTML of the url by class name (can be changed using By import)
try: 
    searched = wait.until(
     EC.presence_of_element_located(By.CLASS_NAME, "YMlIz FpEdX jLMuyc")    
    )
except: 
    print('\nCannot find the text specified!')
    driver.quit()

for name in searched: 
    print(name.text)
    price_of_name = name.find_element(By.CLASS_NAME, "YMlIz FpEdX jLMuyc")

# search = driver.find_element_by_id("main")
# search.send_keys("price")
# search.send_keys(Keys.RETURN)

# delays the program (5 sec) so it doesn't quit instantly.
time.sleep(5)

# Exit driver 
driver.quit()  