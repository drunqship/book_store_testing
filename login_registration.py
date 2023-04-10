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

#  регистрация аккаунта
driver.find_element_by_css_selector('#menu-item-50 a').click()
driver.find_element_by_css_selector('#reg_email').send_keys('joe_biden@whitehouse.com')
driver.find_element_by_css_selector('#reg_password').send_keys('IForgotThePassword')
driver.find_element_by_css_selector('.u-column2.col-2 input.woocommerce-Button.button').click()
driver.quit()

# логин в систему
driver.find_element_by_css_selector('#menu-item-50 a').click()
driver.find_element_by_css_selector('#username').send_keys('joe_biden@whitehouse.com')
driver.find_element_by_css_selector('#password').send_keys('IForgotThePassword')
driver.find_element_by_css_selector('.u-column1.col-1 input.woocommerce-Button.button').click()
assert driver.find_element_by_css_selector('.woocommerce ul li:nth-child(6) a').text == 'Logout'
driver.quit()

