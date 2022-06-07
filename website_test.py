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

time.sleep(0.2)

## Insert password
# secret_password=input(f"What is the password? ")
secret_password='secret_sauce'  
password = driver.find_element_by_id("password")
password.clear() #delete anything previously typed
password.send_keys(secret_password)
time.sleep(0.2)

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

## Case 1- Buy one object
def buy_products(n):
    purchased_items=random.sample(cart_buttons,n)
    for each in purchased_items:
        each.click()
        time.sleep(1)
    return()

how_many=int(input(f"how many products you want to buy? "))
buy_products(how_many) #This is a random way to select products, but it can 
#be made that for a specific set of products proceeds with that selection


link=driver.find_element_by_class_name("shopping_cart_link")
link.click()
time.sleep(2)

## To pay

##TODO in the page https://www.saucedemo.com/cart.html, make sure that the right price applied
## for each object 

# driver.close()