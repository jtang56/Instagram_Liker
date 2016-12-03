username = "" #username goes here
password = "" #password goes here

users = [] #usernames to like goes here

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Open Instagram in Firefox and wait for the login form to load
browser = webdriver.Firefox()
browser.get('https://instagram.com/')
browser.maximize_window()
time.sleep(2)

# Click the link to go to the login form
#login_link = browser.find_element_by_css_selector('_fcn8k')
login_link = browser.find_element_by_class_name('_fcn8k')
login_link.click()

# Enter username
username_input = browser.find_element_by_css_selector('div._ccek6:nth-child(1) > input:nth-child(1)')
username_input.send_keys(username)

# Enter password
password_input = browser.find_element_by_css_selector('div._ccek6:nth-child(2) > input:nth-child(1)')
password_input.send_keys(password)

# Login
password_input.submit()

time.sleep(5)

while True:
	# Like all the images that are loaded on login
	#for like_link in browser.find_elements_by_link_text('Like'):
    	#print like_link.getText()
		#like_link.click()

	for x in browser.find_elements_by_class_name('_8ab8k'):
		y = x.find_element_by_class_name('_s6yvg')
		for temp_user in users:
			if temp_user in y.text:
				try:
					z = x.find_element_by_link_text('Like')
					z.click()
					print y.text + " at " + str(datetime.now())
				except NoSuchElementException:
					pass
	time.sleep(2)
	browser.get('https://instagram.com/')
	#time.sleep(2)
# Close the tab/browser when done
#browser.close()
