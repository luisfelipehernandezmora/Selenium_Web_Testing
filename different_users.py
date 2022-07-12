"""
In this file we will test different users that on before hand we know they give problems, 
so we want to be able to trace those problems
"""
import random
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import logging
from time import gmtime, strftime
import os
from selenium.common.exceptions import ScreenshotException
 

def timeit():
    return (strftime("%H:%M:%S", gmtime()))

waiting_time=1
users=["standard_user","locked_out_user","problem_user","performance_glitch_user","one_new_user"]
ask=None

while ask not in range(1,6):
    
    ask=int(input(f"""Which user we are will test?
1. standard_user            (it wont give any problem :) )
2. locked_out_user          (is banned from the website)
3. problem_user             (will suffer a lot of problems)
4. performance_glitch_user  (will be a little stuck while browsing)
5. one_new_user             (don't even exist)
"""))

    if ask==1:
        selected_user="standard_user"
    elif ask==2:
        selected_user="locked_out_user"
    elif ask==3:
        selected_user="problem_user"
    elif ask==4:
        selected_user="performance_glitch_user"
    elif ask==5:
        selected_user="one_new_user"

print(f"The selected user is {selected_user}")
secret_password='secret_sauce'  

## Logger section
##TODO
# Understand what is timeit 
logger = logging.getLogger('timeit') 

day=time.strftime("%D").replace("/","_")
log_name=f"log{day}-{selected_user}.log"
current_dir=os.getcwd()
path=str(current_dir)+str("/logs")

##TODO
# Convert to pathlib.path and pass object that to the hdlr
hdlr = logging.FileHandler(fr'C:\Users\adarsh\Desktop\Luis_Felipe\Tech_talk\logs\{log_name}')


# hdlr = logging.FileHandler(fr'\{current_dir}\logs\{log_name}')
formatter = logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

logger.info(timeit())
logger.info(f"New testing session begin\n")
logger.info(f"The selected user is {selected_user} with password as {secret_password}\n")

## OPTIONS FOR THE SELENIUM BROWSER
options= webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080")

url="https://www.saucedemo.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
time.sleep(waiting_time)

## Insert User name
user_name = driver.find_element_by_id("user-name")
user_name.clear() #delete anything previously typed
user_name.send_keys(selected_user)
time.sleep(waiting_time)

## Insert password
# secret_password=input(f"What is the password? ")
password = driver.find_element_by_id("password")
password.clear() #delete anything previously typed
password.send_keys(secret_password)
time.sleep(waiting_time)

## Click the login button #Here user 2 and 5 will fail and not continue

login=driver.find_element_by_id("login-button")
login.click()
current_URL=driver.current_url

if current_URL=="https://www.saucedemo.com/inventory.html":
    print(f"Succesful login with user {selected_user} and password {secret_password}")
    logger.info(timeit())
    logger.info(f"Succesful login with user {selected_user} and password {secret_password}")
else:
    message=driver.find_element_by_tag_name("h3").accessible_name

    if message=="Epic sadface: Sorry, this user has been locked out.":
        print(f"A problem while login happened with user: {selected_user} and password: {secret_password}\n{message}")
        logger.info(timeit())
        logger.info(f"A problem while login happened with user: {selected_user} and password: {secret_password}\n{message}")
    elif message=="Epic sadface: Username and password do not match any user in this service":
        print(f"A problem while login happened with user: {selected_user} and password: {secret_password}\n{message}")
        logger.info(timeit())
        logger.info(f"A problem while login happened with user: {selected_user} and password: {secret_password}\n{message}")
    driver.close()
    quit()

## Take a screenshot here
try:
    ## File name for the screenshot
    screenshot_id = day +"_"+str(time.strftime("%H %M %S"))+"_"+selected_user+".png"
    ## ATENTION the folder "screenshots" have to be created before, otherwise the driver 
    # will not save the screenshot
    driver.save_screenshot(fr'C:\Users\adarsh\Desktop\Luis_Felipe\Tech_talk\screenshots\{screenshot_id}')
    # driver.save_screenshot(f'{screenshot_id}')

    logger.info(timeit())
    logger.info(f"Screenshot saved succesfully with the name {screenshot_id}")
except ScreenshotException as e:
    print(f"A {e} occurred")
    logger.error(f"A {e} occurred")
    screenshot_id = "NaN"

## Click in something
# all_buttons=driver.find_elements_by_class_name("inventory_item_price")
all_buttons=driver.find_elements_by_tag_name("button")
cart_buttons=[]
for button in all_buttons:
    if button.text=='ADD TO CART':
        cart_buttons.append(button)

## Case 1- Buy one object
def buy_products(n,cart_buttons):
    purchased_items=random.sample(cart_buttons,n)
    for each in purchased_items:
        each.click()
        time.sleep(waiting_time)
    return()

how_many=int(input(f"\nHow many products you want to buy?\n"))
buy_products(how_many,cart_buttons) #This is a random way to select products, but it can 
#be made that for a specific set of products proceeds with that selection


link=driver.find_element_by_class_name("shopping_cart_link")
link.click()
time.sleep(waiting_time)

##Count the items
items_marked=driver.find_element_by_class_name("shopping_cart_badge").text
items_marked=int(items_marked)
if items_marked!=how_many:
    print(f"Oh wait! the page is not recording all the desired items")
    logger.info(timeit())
    logger.info(f"Oh wait! with user: {selected_user} the page is not recording all the desired items")
    driver.close()
    quit()

## To proceed with paynment
proceed=driver.find_element_by_id("checkout")
proceed.click()
time.sleep(waiting_time)

first_name=driver.find_element_by_id("first-name")
first_name.clear()
first_name.send_keys("luis")
time.sleep(waiting_time-0.5)

last_name=driver.find_element_by_id("last-name")
last_name.clear()
last_name.send_keys("Hernandez")
time.sleep(waiting_time-0.5)

zip_code=driver.find_element_by_id("postal-code")
zip_code.clear()
zip_code.send_keys("10701")
time.sleep(waiting_time-0.5)

continue_button=driver.find_element_by_id("continue")
continue_button.click()
time.sleep(waiting_time-0.2)

##TODO in the page https://www.saucedemo.com/checkout-step-two.html make sure 
# that the right price applied for each object and that the total sum is same 
# as item total and somehow guess the tax and see that all is ok!

finish=driver.find_element_by_id("finish")
time.sleep(waiting_time)
finish.click()
driver.close()