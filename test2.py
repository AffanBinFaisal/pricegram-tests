from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

edge_driver_path = 'msedgedriver.exe'

driver = webdriver.Edge(executable_path=edge_driver_path)

driver.maximize_window()

driver.get('http://10.7.231.25:3000/')

time.sleep(1)

search_box = driver.find_element_by_class_name('Navbar-searchbar ')
search_box.send_keys("Hp")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

filter_button = driver.find_element_by_class_name('Filter-main-button')
filter_button.click()

time.sleep(1)

select_button = driver.find_element_by_class_name('SelectionMenu-button')
select_button.click()

time.sleep(1)

option = driver.find_element_by_xpath('//*[@id="options"]/option[3]')
option.click()

time.sleep(1)

checkbox = driver.find_element_by_xpath('//*[@id="myDropdown1"]/div/div[2]/div[2]/div[1]/label[2]/span')
checkbox.click()

time.sleep(1)
select_button = driver.find_element_by_class_name('Filter-button')
select_button.click()