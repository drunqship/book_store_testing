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

# отображение страницы товара
driver.find_element_by_css_selector('#menu-item-50 a').click()
driver.find_element_by_css_selector('#username').send_keys('joe_biden@whitehouse.com')
driver.find_element_by_css_selector('#password').send_keys('IForgotThePassword')
driver.find_element_by_css_selector('.u-column1.col-1 input.woocommerce-Button.button').click()
driver.find_element_by_css_selector('#menu-item-40 a').click()
driver.find_element_by_css_selector('#content .products li:nth-child(3) a img').click()
book_title = driver.find_element_by_css_selector('.summary .product_title').text
if book_title == 'HTML5 Forms':
    print('Название правильное')
else:
    print('Название неправильное')
driver.quit()

# количество товаров в категории
driver.find_element_by_css_selector('#menu-item-50 a').click()
driver.find_element_by_css_selector('#username').send_keys('joe_biden@whitehouse.com')
driver.find_element_by_css_selector('#password').send_keys('IForgotThePassword')
driver.find_element_by_css_selector('.u-column1.col-1 input.woocommerce-Button.button').click()
driver.find_element_by_css_selector('#menu-item-40 a').click()
driver.find_element_by_css_selector('.cat-item-19 a').click()
time.sleep(3)
items_count = driver.find_elements_by_css_selector('ul li a img')
if len(items_count) == 3:
    print('В категории HTML 3 товара')
else:
    print('Ошибка. Количество товаров в категории HTML:', str(len(items_count)))
driver.quit()

# сортировка товаров
driver.find_element_by_css_selector('#menu-item-50 a').click()
driver.find_element_by_css_selector('#username').send_keys('joe_biden@whitehouse.com')
driver.find_element_by_css_selector('#password').send_keys('IForgotThePassword')
driver.find_element_by_css_selector('.u-column1.col-1 input.woocommerce-Button.button').click()
driver.find_element_by_css_selector('#menu-item-40 a').click()
assert driver.find_element_by_css_selector('select.orderby').get_attribute('value') == 'menu_order'
Select(driver.find_element_by_css_selector('.orderby')).select_by_value('price-desc')
assert driver.find_element_by_css_selector('select.orderby').get_attribute('value') == 'price-desc'
driver.quit()

# отображение, скидка товара
driver.find_element_by_css_selector('#menu-item-50 a').click()
driver.find_element_by_css_selector('#username').send_keys('joe_biden@whitehouse.com')
driver.find_element_by_css_selector('#password').send_keys('IForgotThePassword')
driver.find_element_by_css_selector('.u-column1.col-1 input.woocommerce-Button.button').click()
driver.find_element_by_css_selector('#menu-item-40 a').click()
driver.find_element_by_css_selector('ul li:nth-child(1) a img').click()
assert driver.find_element_by_css_selector('.price del span.woocommerce-Price-amount').text == '₹600.00'
assert driver.find_element_by_css_selector('.price ins').text == '₹450.00'
wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.images img'))).click()
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close'))).click()
driver.quit()

# проверка цены в корзине (на сайте доступна только одна книга, все тесты я провёл с одним товаром)
driver.find_element_by_css_selector('#menu-item-40 a').click()
driver.execute_script('window.scrollBy(0, 300);')
driver.find_element_by_css_selector('ul.products.masonry-done li:nth-child(6) a.button').click()
time.sleep(3)
assert driver.find_element_by_css_selector('.wpmenucart-contents .cartcontents').text == '1 Item'
assert driver.find_element_by_css_selector('.wpmenucart-contents .amount').text == '₹350.00'
driver.find_element_by_css_selector('.wpmenucart-contents').click()
wait = WebDriverWait(driver, 10)
wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal'), '₹350.00'))
wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total'), '₹357.00'))
driver.quit()

# работа в корзине (на сайте доступна только одна книга, все тесты я провёл с одним товаром)
driver.find_element_by_css_selector('#menu-item-40 a').click()
driver.execute_script('window.scrollBy(0, 300);')
time.sleep(1)
driver.find_element_by_css_selector('ul.products.masonry-done li:nth-child(6) a.button').click()
time.sleep(1)
driver.find_element_by_css_selector('.wpmenucart-contents').click()
time.sleep(3)
driver.find_element_by_css_selector('.product-remove a').click()
time.sleep(1)
driver.find_element_by_css_selector('.woocommerce-message a').click()
driver.find_element_by_css_selector('.quantity input').clear()
driver.find_element_by_css_selector('.quantity input').send_keys('3')
driver.find_element_by_css_selector('.actions .button:nth-child(2)').click()
assert driver.find_element_by_css_selector('.quantity input').get_attribute('value') == '3'
time.sleep(1)
driver.find_element_by_css_selector('.actions .coupon .button').click()
assert driver.find_element_by_css_selector('.woocommerce-error li').text == 'Please enter a coupon code.'
driver.quit()

# покупка товара
driver.find_element_by_css_selector('#menu-item-40 a').click()
driver.execute_script('window.scrollBy(0, 300);')
time.sleep(1)
driver.find_element_by_css_selector('ul.products.masonry-done li:nth-child(6) a.button').click()
time.sleep(1)
driver.find_element_by_css_selector('.wpmenucart-contents').click()
wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout a'))).click()
wait.until(ec.url_to_be('https://practice.automationtesting.in/checkout/'))
driver.find_element_by_css_selector('#billing_first_name').send_keys('Joe')
driver.find_element_by_css_selector('#billing_last_name').send_keys('Biden')
driver.find_element_by_css_selector('#billing_email').send_keys('joe_biden@whitehouse.com')
driver.find_element_by_css_selector('#billing_phone').send_keys('2298511269')
driver.find_element_by_css_selector('#s2id_billing_country').click()
driver.find_element_by_css_selector('#s2id_autogen1_search').send_keys('United')
driver.find_element_by_css_selector('div.select2-drop ul li:nth-child(3)').click()
driver.find_element_by_css_selector('input#billing_address_1').send_keys('Pennsylvania Ave NW Washington')
driver.find_element_by_css_selector('input#billing_city').send_keys('Washington')
driver.find_element_by_css_selector('#select2-chosen-2').click()
driver.find_element_by_css_selector('#s2id_autogen2_search').send_keys('District')
driver.find_element_by_css_selector('div.select2-drop ul li').click()
driver.find_element_by_css_selector('#billing_postcode').send_keys('20500')
# driver.execute_script('window.scrollBy(0, 600);') # при добавлении прокрутки тест ломается, без неё всё работает нормально
# time.sleep(1)
driver.find_element_by_css_selector('.wc_payment_method.payment_method_cheque label').click()
driver.find_element_by_css_selector('#place_order').click()
wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'tfoot tr:nth-child(3) td'), 'Check Payments'))
driver.quit()