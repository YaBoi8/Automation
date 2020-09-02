from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
'''#  Отображение страницы товара
#  Открытие
driver.get("http://practice.automationtesting.in/")
#  Логин
My_Acc = driver.find_element_by_id('menu-item-50').click()
Login_email = driver.find_element_by_id('username').send_keys('yaboi@test.com')
Login_password = driver.find_element_by_id('password').send_keys('Testyaboi#')
Login_btn = driver.find_element_by_name('login').click()
#  Shop
Shop = driver.find_element_by_id('menu-item-40').click()
Book = driver.find_element_by_css_selector('.post-181>[rel=nofollow]').click()
# Проверка имени
Book_name = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'product_title'), "HTML5 Forms"))
#  Закрытие
driver.quit()'''
##############################
#  Количество товаров в категории
'''#  Открытие
driver.get("http://practice.automationtesting.in/")
#  Логин
My_Acc = driver.find_element_by_id('menu-item-50').click()
Login_email = driver.find_element_by_id('username').send_keys('yaboi@test.com')
Login_password = driver.find_element_by_id('password').send_keys('Testyaboi#')
Login_btn = driver.find_element_by_name('login').click()
#  Shop
Shop = driver.find_element_by_id('menu-item-40').click()
HTML_cat = driver.find_element_by_css_selector(".cat-item-19>a").click()
Books_count = driver.find_elements_by_class_name('price')
if len(Books_count) == 3:
    print("Количество книг: 3")
else:
    print("Количество книг: " + str(len(Books_count)))
#  Закрытие
driver.quit()'''
###########################
#  Сортировка товара
'''#  Открытие
driver.get("http://practice.automationtesting.in/")
#  Логин
My_Acc = driver.find_element_by_id('menu-item-50').click()
Login_email = driver.find_element_by_id('username').send_keys('yaboi@test.com')
Login_password = driver.find_element_by_id('password').send_keys('Testyaboi#')
Login_btn = driver.find_element_by_name('login').click()
#  Shop
Shop = driver.find_element_by_id('menu-item-40').click()
# Проверка селектора
High_to_low = driver.find_element_by_css_selector('[value=price-desc]')
High_to_low_selected = High_to_low.get_attribute("selected")
if High_to_low_selected is None:
    print("Селектор не выбран")
else:
    print("Селектор выбран")
#  Выбор селектора
htl = driver.find_element_by_class_name("orderby")
select = Select(htl)
select.select_by_value("price-desc")
# Проверка селектора
High_to_low = driver.find_element_by_css_selector('[value=price-desc]')
High_to_low_selected = High_to_low.get_attribute("selected")
if High_to_low_selected is None:
    print("Селектор не выбран")
else:
    print("Селектор выбран")
#  Закрытие
driver.quit()'''
#######################
#  Отображение, скидка товара
'''#  Открытие
driver.get("http://practice.automationtesting.in/")
#  Логин
My_Acc = driver.find_element_by_id('menu-item-50').click()
Login_email = driver.find_element_by_id('username').send_keys('yaboi@test.com')
Login_password = driver.find_element_by_id('password').send_keys('Testyaboi#')
Login_btn = driver.find_element_by_name('login').click()
#  Shop
Shop = driver.find_element_by_id('menu-item-40').click()
#  Выбор книги
Guide = driver.find_element_by_css_selector(".post-169>a:nth-child(2)").click()
#  Проверка старой цены
old_price = driver.find_element_by_css_selector('.price>del>span')
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
#  Проверка новой цены
new_price = driver.find_element_by_css_selector(".price>ins>span")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
#  Открытие картинки
wait = WebDriverWait(driver, 30)
Img = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-main-image.zoom"))).click()
#  Закрытие картинки
Close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
#  Закрытие
driver.quit()'''
####################
#  Проверка цены в корзине
'''#  Открытие
driver.get("http://practice.automationtesting.in/")
#  Shop
Shop = driver.find_element_by_id('menu-item-40').click()
#  Добавление книги в корзину
Add = driver.find_element_by_css_selector(".post-182>[rel='nofollow']").click()
#  Проверка количества и цены
price = driver.find_element_by_class_name("cartcontents")
price_text = price.text
assert price_text == "1 Item"
quantity = driver.find_element_by_class_name("amount")
quantity_text = quantity.text
assert quantity_text == "₹180.00"
#  Переход в корзину
Basket = driver.find_element_by_class_name("cartcontents").click()
#  Проверка цены в Subtotal
wait = WebDriverWait(driver, 30)
Subtotal = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'cart-subtotal'), "₹180.00"))
#  Закрытие
driver.quit()'''
########################
#  Работа в корзине
'''#  Открытие
driver.get("http://practice.automationtesting.in/")
#  Shop
Shop = driver.find_element_by_id('menu-item-40').click()
#  Добавление книг в корзину
driver.execute_script('window.scrollBy(0,300)')
Add_WebApp = driver.find_element_by_css_selector(".post-182>[rel='nofollow']").click()
time.sleep(2)
Add_JS = driver.find_element_by_css_selector(".post-180>[rel=nofollow]").click()
#  Переход в корзину
Basket = driver.find_element_by_class_name("cartcontents").click()
time.sleep(2)
#  Удаление первой книги
Del = driver.find_element_by_css_selector(".product-remove>[data-product_id='182']").click()
#  Отмена удаления
Undo = driver.find_element_by_css_selector(".woocommerce-message>a").click()
#  Увеличение количества
Clear = driver.find_element_by_css_selector(".cart_item:nth-child(1)>.product-quantity>.quantity>input").clear()
Add_qty = driver.find_element_by_css_selector(".cart_item:nth-child(1)>.product-quantity>.quantity>input").send_keys("3")
#  Обновление корзины
Update = driver.find_element_by_css_selector(".actions>.button").click()
#  Проверка количесва JS
Quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1)>.product-quantity>.quantity>[value='3']")
Quantity_value = Quantity.get_attribute("value")
assert Quantity_value == "3"
time.sleep(2)
#  Купон
Coupon = driver.find_element_by_css_selector(".coupon>.button").click()
#  Проверка текста купона
Coupon_error = driver.find_element_by_css_selector(".woocommerce-error>li")
Coupon_error_text = Coupon_error.text
assert Coupon_error_text == "Please enter a coupon code."
#  Закрытие
driver.quit()'''
##################
#  Покупка товара
#  Открытие
driver.get("http://practice.automationtesting.in/")
#  Shop
Shop = driver.find_element_by_id('menu-item-40').click()
#  Скролл
driver.execute_script("window.scrollBy(0,300)")
#  Добавление в корзину
Add_WebApp = driver.find_element_by_css_selector(".post-182>[rel='nofollow']").click()
#  Переход в корзину
Basket = driver.find_element_by_class_name("cartcontents").click()
#  Нажать Proceed
wait = WebDriverWait(driver, 30)
Proceed = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a"))).click()
#  Заполнение полей
First = wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name"))).send_keys("Michael")
Last = driver.find_element_by_id("billing_last_name").send_keys("Myers")
Email = driver.find_element_by_id("billing_email").send_keys("MicgaelM@test.com")
Phone = driver.find_element_by_id("billing_phone").send_keys(311019788)
#  Селектор Country
Selector_drop = driver.find_element_by_id("s2id_billing_country").click()
Selector_search = driver.find_element_by_id("s2id_autogen1_search").send_keys("United States (US)")
Selector_select = driver.find_element_by_css_selector("#select2-results-1>li:nth-child(1)").click()
#
Address = driver.find_element_by_id("billing_address_1").send_keys("157 Montrose Ave")
City = driver.find_element_by_id("billing_city").send_keys("Haddonfield")
# Слектрор штата
Selector_state_drop = driver.find_element_by_id("s2id_billing_state").click()
Selector_state_search = driver.find_element_by_id("s2id_autogen404_search").send_keys("Illinois")
Selector_state_select = driver.find_element_by_class_name("select2-results-dept-0").click()
#
ZIP = driver.find_element_by_id("billing_postcode").send_keys("31108")
#  Выбор способа оплаты
driver.execute_script('window.scrollBy(0,600)')
time.sleep(2)
Check_payments = driver.find_element_by_id("payment_method_cheque").click()
Place_order = driver.find_element_by_id("place_order").click()
#  Проверка текста
Thank = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
Pay_method = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.shop_table>tfoot>tr:nth-child(3)'), "Check Payments"))
#  Закрытие
driver.quit()
