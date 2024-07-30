from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

edge_driver_path = 'msedgedriver.exe'

driver = webdriver.Edge(executable_path=edge_driver_path)

driver.get('http://10.7.231.25:3000/')
driver.maximize_window()

time.sleep(1)

search_box = driver.find_element_by_class_name('Navbar-searchbar ')
search_box.send_keys("Hp")
search_box.send_keys(Keys.RETURN)