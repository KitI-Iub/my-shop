##Home: добавление комментария##

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby_book = driver.find_element_by_id("text-22-sub_row_1-0-2-0-0").click()
reviews_btn = driver.find_element_by_css_selector(".reviews_tab").click()
rating_stars = driver.find_element_by_css_selector(".stars .star-5").click()
review_field = driver.find_element_by_id("comment")
review_field.send_keys("Nice book!")
name_field = driver.find_element_by_id("author")
name_field.send_keys("Name")
emai_field = driver.find_element_by_id("email")
emai_field.send_keys("email@mail.com")
submit_btn = driver.find_element_by_id("submit").click()
driver.quit()