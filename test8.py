from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

edge_driver_path = 'msedgedriver.exe'

driver = webdriver.Edge(executable_path=edge_driver_path)

driver.maximize_window()

driver.get('http://10.7.231.25:3000/authorize/')

time.sleep(3)

username_field = driver.find_element_by_xpath('//*[@id="__next"]/main/div/center/div/div/div/form/input[1]')
username_field.send_keys('lord1')

password_field = driver.find_element_by_xpath('//*[@id="__next"]/main/div/center/div/div/div/form/input[2]')
password_field.send_keys('lord')

login_button = driver.find_element_by_xpath('//*[@id="__next"]/main/div/center/div/div/div/form/button')
login_button.click()

time.sleep(5)

menu_button = driver.find_element_by_xpath('//*[@id="navbarMain"]/header/button[1]')
menu_button.click()

report_button = driver.find_element_by_xpath('//*[@id="myDropdown"]/div[5]/button[2]/a')
report_button.click()