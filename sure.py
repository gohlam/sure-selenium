# Selenium Code that tests WizeHive with 400 Apps for the Sure Program 
# Created by Allison Gohl; uniqname = gohla 

from time import sleep
import time
from ConfigParser import ConfigParser
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, \
		ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#global URL
URL = https://app.wizehive.com/appform/login/sure
def main():
	#prompt the user for their uniqname as the main email base
	uniqname = input("Please enter your uniqname: ")
	password = input("Please choose a password: ")
	#make the driver to run this script, using Google Chrome which requires chrome driver
	driver = webdriver.Chrome('./chromedriver')
	#put inside a for loop for 400 apps
	#for(var i = 0; i < 400; i++)
	#go to the sign up page each time
	driver.get(URL)
	#login/sign up using WizeHive
	signUp(driver, uniqname, password, i)
	#fill out app
	fillOutApp(driver)
	#upload pdf

	#submit form

	driver.quit()
main()

def signUp(driver, uniqname, password, i):
	#input the email and password to sign up for SURE
	sign = driver.find_element_by_id('SignupEmail')
	email = uniqname + str(i) + '@umich.edu'
	sign.send_keys(email, Keys.TAB)
	pass = driver.find_element_by_id('password2')
	pass.send_keys(password, Keys.TAB)
	#enter the password a second time and login
	pass = driver.find_element_by_id('ConfirmPassword')
	pass.send_keys(password, Keys.TAB, Keys.ENTER)
	#fill out app
	#?????????? EMAIL
	fillOutApp(driver, email)

def fillOutApp(driver, email):
	first = driver.find_element_by_id('field1377224')
	#enter the first name
	first.send_keys(first, Keys.TAB)
	#enter the last name
	driver.send_keys(last, Keys.TAB)
	#select the woman option under the gender dropdown
	driver.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
	email = 
