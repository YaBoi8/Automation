from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#  Открытие
driver.get("http://practice.automationtesting.in/")
#  Скролл
driver.execute_script("window.scrollBy(0,600)")
#  Открытие страницы книги
Ruby = driver.find_element_by_css_selector('.post-160>[rel=nofollow]').click()
#  Отзыв
Reviews = driver.find_element_by_class_name('reviews_tab').click()
#  5 звёзд
Star = driver.find_element_by_class_name('star-5').click()
# Сомммент
Comment = driver.find_element_by_id('comment').send_keys('Nice book!')
#  Имя
Name = driver.find_element_by_id('author').send_keys('YaBoi')
#  Email
Email = driver.find_element_by_id('email').send_keys('yaboi@test.com')
#  Отправка отзыва
Submit = driver.find_element_by_id('submit').click()
#  Закрытие
driver.quit()
