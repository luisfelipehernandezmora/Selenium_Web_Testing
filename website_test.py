## Example taken from "https://pythonspot.com/selenium-click-button/"

from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

url="https://www.saucedemo.com/"
options= webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
# time.sleep(2.5)

# assert "Swag Labs" in driver.title

selected_user=input(f"""\nWhich user you will like to use? You can choose between\n
    standard_user (it wont give any problem :) ),
    locked_out_user (is banned from the website). 
    problem_user (will suffer a lot of problems), 
    performance_glitch_user (will be a little stuck while browsing) \n\n""")

## Insert User name
user_name = driver.find_element_by_id("user-name")
user_name.clear() #delete anything previously typed
user_name.send_keys(selected_user)

time.sleep(2.5)

## Insert password
# secret_password=input(f"What is the password? ")
secret_password='secret_sauce'  
password = driver.find_element_by_id("password")
password.clear() #delete anything previously typed
password.send_keys(secret_password)
time.sleep(2.5)

driver.close()