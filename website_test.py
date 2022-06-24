import random
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

waiting_time=1

url="https://www.saucedemo.com/"
options= webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--test-type')
options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
time.sleep(waiting_time)

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

time.sleep(waiting_time)

## Insert password
# secret_password=input(f"What is the password? ")
secret_password='secret_sauce'  
password = driver.find_element_by_id("password")
password.clear() #delete anything previously typed
password.send_keys(secret_password)
time.sleep(waiting_time)

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
        time.sleep(waiting_time)
    return()

how_many=int(input(f"\nHow many products you want to buy?\n"))
buy_products(how_many) #This is a random way to select products, but it can 
#be made that for a specific set of products proceeds with that selection


link=driver.find_element_by_class_name("shopping_cart_link")
link.click()
time.sleep(waiting_time)

## To proceed with paynment
proceed=driver.find_element_by_id("checkout")
proceed.click()
time.sleep(waiting_time)

first_name=driver.find_element_by_id("first-name")
first_name.clear()
first_name.send_keys("luis")
time.sleep(waiting_time)

last_name=driver.find_element_by_id("last-name")
last_name.clear()
last_name.send_keys("Hernandez")
time.sleep(waiting_time)

zip_code=driver.find_element_by_id("postal-code")
zip_code.clear()
zip_code.send_keys("10701")
time.sleep(waiting_time)

continue_button=driver.find_element_by_id("continue")
continue_button.click()
time.sleep(waiting_time)

##TODO in the page https://www.saucedemo.com/checkout-step-two.html make sure 
# that the right price applied for each object and that the total sum is same 
# as item total and somehow guess the tax and see that all is ok!

finish=driver.find_element_by_id("finish")
time.sleep(waiting_time)
finish.click()
driver.close()