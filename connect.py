# connect python with webbrowser-chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag




def main():
    # url of LinkedIn
    url = “http://linkedin.com/"  
    # url of LinkedIn network page
    network_url = “http://linkedin.com / mynetwork/" 
    # path to browser web driver
    driver = webdriver.Chrome('C:\\Program Files\\Web Driver\\chromedriver.exe'')
    driver.get(url)

# Driver's code
if __name__ == __main__:
    main()