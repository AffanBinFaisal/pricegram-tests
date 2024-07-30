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

time.sleep(2)

explore_button = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div/div[1]/div/div/div[1]/a[2]/button')
explore_button.click()

time.sleep(2)

buy_button = driver.find_element_by_class_name('PageHead-buy')
buy_button.click()