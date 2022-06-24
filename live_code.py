
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

url="https://www.saucedemo.com/"
options= webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
time.sleep(2)

## Insert User name
selected_user="problem_user"
user_name = driver.find_element_by_id("user-name")
user_name.clear() #delete anything previously typed
user_name.send_keys(selected_user)
time.sleep(0.5)

## Insert password
secret_password='secret_sauce'  
password = driver.find_element_by_id("password")
password.clear() #delete anything previously typed
password.send_keys(secret_password)
time.sleep(0.2)

## Click the login button
login=driver.find_element_by_id("login-button")
login.click()
time.sleep(2)

## Click in something
all_buttons=driver.find_elements_by_tag_name("button")
cart_buttons=[]
for button in all_buttons:
    if button.text=='ADD TO CART':
        cart_buttons.append(button)

def buy_products(n):
    purchased_items=random.sample(cart_buttons,n)
    for each in purchased_items:
        each.click()
        time.sleep(2)
    return()

how_many=int(input(f"how many products you want to buy? "))
buy_products(how_many) #This is a random way to select products, but it can 
#be made that for a specific set of products proceeds with that selection

link=driver.find_element_by_class_name("shopping_cart_link")
link.click()
time.sleep(2)

## To proceed with paynment
proceed=driver.find_element_by_id("checkout")
proceed.click()
time.sleep(0.5)

first_name=driver.find_element_by_id("first-name")
first_name.clear()
first_name.send_keys("luis")
time.sleep(0.3)

last_name=driver.find_element_by_id("last-name")
last_name.clear()
last_name.send_keys("Hernandez")
time.sleep(0.3)

zip_code=driver.find_element_by_id("postal-code")
zip_code.clear()
zip_code.send_keys("10701")
time.sleep(0.3)

continue_button=driver.find_element_by_id("continue")
continue_button.click()
time.sleep(0.2)

finish=driver.find_element_by_id("finish")
finish.click()
time.sleep(0.2)
driver.close()
