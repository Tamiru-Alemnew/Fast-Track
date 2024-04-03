# connect python with webbrowser-chrome
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


import pyautogui as pag

PATH = "path/to/chromedriver"

chrome_options = Options()

# Add any options you want (this line is optional)
driver = webdriver.Chrome( options=chrome_options)   

def login():

	# Getting the login element
	username = driver.find_element(By.ID,  "login-email") 

	# Sending the keys for username	 
	username.send_keys("teshome-birhanu")

	# Getting the password element								 
	password = driver.find_element(By.ID, "login-password")

	# Sending the keys for password 
	password.send_keys("T21288445702406.")	 

	# Getting the tag for submit button					 
	driver.find_element(By.ID, "login-submit").click()
	goto_network()		 

def goto_network():
	driver.find_element(By.ID, "mynetwork-tab-icon").click()
	send_requests()

def send_requests():

	# Number of requests you want to send
	n = input("Number of requests: ") 

	for i in range(0, n):
		# position(in px) of connection button
		pag.click(880, 770) 
	print("Done !")

def main():
 
    # url of LinkedIn
    url = "http://linkedin.com/" 
 
    # url of LinkedIn network page
    network_url = "http://linkedin.com / mynetwork/"  
 
    # path to browser web driver
	# Create a ChromeOptions object
  
    driver.get(url)
	
    login()

# Driver's code 
if __name__ == "__main__":
	main()
