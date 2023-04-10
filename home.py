import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://practice.automationtesting.in/')

# добавление комментария
driver.execute_script('window.scrollBy(0, 600);')
driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 a img').click()
driver.find_element_by_css_selector('.reviews_tab').click()
driver.execute_script('window.scrollBy(0, 500);')
driver.find_element_by_css_selector('.star-5').click()
driver.find_element_by_css_selector('textarea#comment').send_keys('Nice book!')
driver.find_element_by_css_selector('input#author').send_keys('Joe Biden')
driver.find_element_by_css_selector('#email').send_keys('joe_biden@whitehouse.com')
driver.find_element_by_css_selector('.submit').click()
driver.quit()
