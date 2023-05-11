##Registration_login: регистрация аккаунта##


from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)

my_account = driver.find_element_by_link_text("My Account").click()
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("testtteeessstttest@gmail.com")
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("Test1P@ss_worD")
reg_btn = driver.find_element_by_name("register").click()
driver.quit()


##Registration_login: логин в систему##

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)

my_account = driver.find_element_by_link_text("My Account").click()
reg_email = driver.find_element_by_id("username")
reg_email.send_keys("testtteeessstttest@gmail.com")
reg_password = driver.find_element_by_id("password")
reg_password.send_keys("Test1P@ss_worD")
reg_btn = driver.find_element_by_name("login").click()
logout_btn = driver.find_element_by_link_text("Logout")
if logout_btn is not None:
    print("Элемент 'Logout' есть на странице")
else:
    print("Элемента 'Logout' нет на странице")
driver.quit()