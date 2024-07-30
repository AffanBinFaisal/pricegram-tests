from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

edge_driver_path = 'msedgedriver.exe'

driver = webdriver.Edge(executable_path=edge_driver_path)

driver.maximize_window()

driver.get('http://10.7.231.25:3000/authorize')

time.sleep(3)

username_field = driver.find_element_by_xpath('//*[@id="__next"]/main/div/center/div/div/div/form/input[1]')
username_field.send_keys('lord1')

password_field = driver.find_element_by_xpath('//*[@id="__next"]/main/div/center/div/div/div/form/input[2]')
password_field.send_keys('lord')

login_button = driver.find_element_by_xpath('//*[@id="__next"]/main/div/center/div/div/div/form/button')
login_button.click()

time.sleep(10)

search_box = driver.find_element_by_class_name('Navbar-searchbar ')
search_box.send_keys("Hp")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

explore_button = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div/div[1]/div/div/div[1]/a[2]/button')
explore_button.click()

time.sleep(3)

fav_button = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div/div[1]/div/div/div[1]/div/button[2]')
fav_button.click()

like_button = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div/div[1]/div/div/div[1]/div/button[3]')
like_button.click()
