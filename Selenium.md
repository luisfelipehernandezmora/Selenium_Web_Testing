# Webscraping and automate testing with Selenium (Tech Talk 14th july)

## Introduction

### What is it?

Is an **open source** project, that provides many automation capabilities and webscraping elements. is said that requires **higher coding skills** when compared with other web testing comercial softwares (all of them paid). Supports **multiple programming languages** like Java, Python, CSharp, Ruby, JavaScript and Kotlin. It's official documentation can be found [here](https://www.selenium.dev/documentation/) and a not official documentation, but still very handy, well organized and helpful can be found [here](https://selenium-python.readthedocs.io/index.html)

### What we will do?
1. We are going to explore the different options and capabilities of Selenium 
2. Live-code an example in a test website. 
3. See how to test a webpage with different cases, users, check and detect unexpected behaviors or bugs. 

### What are people going to get after the talk?
1. An overview of the capabilities of this module. 
2. A better idea of how to conduct automate testing for a website when is being develop.
3. One more tool to do webscraping and automate testing

## Requirements
There is a requirements.txt included. <br>
selenium==4.3.0<br>
webdriver_manager==3.5.4

## Description of the project
It consists in 2 python scripts that will test a website that represents an online service where people can buy differents goods. The website to be used is https://www.saucedemo.com/ . This website is intended to help students learn how to perform automate testing using selenium.

The first file is called __website_test.py__, it  shows the process of accesing, clicking, typing and interacting with a webpage. Proceeds trough it's different tabs and conclude a purchase. In order to know the exact name of the elements to be accessed and click, is fundamental to **inspect the webpage** and to also **debug the elements once that you find them**. This last step is needed to know the name of certain attributes of objects like:

```python
for button in all_buttons:
    if button.text=='ADD TO CART':
        cart_buttons.append(button)
```

the `button.text=="ADD TO CART"` is found when debugging the element and looking in it's available atributes.

In this test website, there are a username that works fine, and is the one used in the first script to show the functionality and ilustrate the procedure on how to navigate trough a website. 

in the second script called __different_users__ is included different users that can have some problems with the webpage. This is intended to show different problems that can arise and how can they be found with Selenium. 

Some sections included are:
- Taking screenshots
- Comparing the number of items desired with the number of items picked in the page
- Checking if once the password and username is inserted, the test can proceed beyond that page or is getting blocked.

Also an aditional functionality added for a real test purpose is the looger, which records the events that happen when running each case.

### Comming soon
Although it is true, that selenium was used to verify that the results were as expected; Another way to do this is through the Unittest module. In this case, the functions that verify each one of the procedures (such as having advanced to the correct link, or having the correct number of items in the shopping cart) must be created using Selenium, and then the outputs are compared with the functions available (assert methods) in Unitest.










