from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#  Открытие
driver.get("http://practice.automationtesting.in/")
# Переход в аккаунт
My_Acc = driver.find_element_by_id('menu-item-50')
My_Acc.click()
#  Регистрация
Email = driver.find_element_by_id('reg_email').send_keys('yaboi@test.com')
Password = driver.find_element_by_id('reg_password').send_keys('Testyaboi#')
Reg = driver.find_element_by_name('register').click()
#  Закрытие
driver.quit()
#  Авторизация
#  Открытие
driver.get("http://practice.automationtesting.in/")
# Переход в аккаунт
My_Acc = driver.find_element_by_id('menu-item-50')
My_Acc.click()
# Логин
Login_email = driver.find_element_by_id('username').send_keys('yaboi@test.com')
Login_password = driver.find_element_by_id('password').send_keys('Testyaboi#')
Login_btn = driver.find_element_by_name('login').click()
#  Проверка елемента
logout_element = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce>nav>ul>li:nth-child(6)>a'), "Logout"))
#  Закрытие
driver.quit()
