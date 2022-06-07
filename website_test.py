## Example taken from "https://pythonspot.com/selenium-click-button/"

import random
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
time.sleep(2.5)

# assert "Swag Labs" in driver.title

# selected_user=input(f"""\nWhich user you will like to use? You can choose between\n
#     standard_user (it wont give any problem :) ),
#     locked_out_user (is banned from the website). 
#     problem_user (will suffer a lot of problems), 
#     performance_glitch_user (will be a little stuck while browsing) \n\n""")
selected_user="standard_user"
## Insert User name
user_name = driver.find_element_by_id("user-name")
user_name.clear() #delete anything previously typed
user_name.send_keys(selected_user)

time.sleep(0.5)

## Insert password
# secret_password=input(f"What is the password? ")
secret_password='secret_sauce'  
password = driver.find_element_by_id("password")
password.clear() #delete anything previously typed
password.send_keys(secret_password)
time.sleep(0.5)

## Click the login button
login=driver.find_element_by_id("login-button")
login.click()


## Click in something
# all_buttons=driver.find_elements_by_class_name("inventory_item_price")
all_buttons=driver.find_elements_by_tag_name("button")
cart_buttons=[]
for button in all_buttons:
    if button.text=='ADD TO CART':
        cart_buttons.append(button)

##Case 1- Buy one object
purchased_item=random.sample(cart_buttons,1)
boton=driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
boton.click()
time.sleep(2)

links=driver.find_element_by_class_name("shopping_cart_link")
links.click()
time.sleep(2)
# one_button=random.choice(all_buttons)
# one_button.click()
# one_button
# time.sleep(2.5)




# driver.close()