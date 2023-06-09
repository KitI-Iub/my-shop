##Shop: отображение страницы товара##


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
shop_tab =driver.find_element_by_id("menu-item-40").click()
book = driver.find_element_by_css_selector(".post-181").click()
book_title = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".entry-title"), "HTML5 Forms"))
driver.quit()


##Shop: количество товаров в категории##


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
shop_tab = driver.find_element_by_id("menu-item-40").click()
cat_HTML = driver.find_element_by_class_name("cat-item-19").click()
items_cat = driver.find_elements_by_css_selector(".product_cat-html")
if len(items_cat) == 3:
    print("HTML содержит 3 товара")
else:
    print("Ошибка. HTML содержит товаров: " + str(len(items_cat)))
driver.quit()


##Shop: сортировка товаров##


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
shop_tab = driver.find_element_by_id("menu-item-40").click()
sort_value = driver.find_elements_by_xpath("//option[1]")
if sort_value is not None:
    print("Сортировка по умолчанию")
else:
    print("Сортировка не по умочанию")
hight_to_low = driver.find_element_by_xpath("//option[6]").click()
hight_to_low = driver.find_element_by_xpath("//option[6]")
if hight_to_low is not None:
    print("Сортировка от большего к меньшему")
else:
    print("Сортировка не от большего к меньшему")
driver.quit()


##Shop: отображение, скидка товара##


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
shop_tab = driver.find_element_by_id("menu-item-40").click()
android_qs_book = driver.find_element_by_class_name("post-169").click()
old_price = driver.find_element_by_css_selector(".price > del > span")
old_price_text = old_price.text
new_price = driver.find_element_by_css_selector(".price > ins > span")
new_price_text = new_price.text
assert old_price_text == "₹600.00"
assert new_price_text == "₹450.00"
book_cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images"))).click()
book_cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()
driver.quit()


##Shop: проверка цены в корзине##


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 > a h3")
html5_webapp_development_book.click()
html5_webapp_development_book_add_btn = driver.find_element_by_css_selector(".single_add_to_cart_button")
html5_webapp_development_book_add_btn.click()
basket_item_value = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
basket_item_value_text = basket_item_value.text
assert basket_item_value_text == "1 Item"
basket_price_value = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
basket_price_value_text = basket_price_value.text
assert basket_price_value_text == "₹180.00"
basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()
subtotal_price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
total_price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00"))
driver.quit()


##Shop: работа в корзине##


from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300);")
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
html5_webapp_development_book.click()
time.sleep(3)
html5_webapp_development_book = driver.find_element_by_css_selector(".post-180 .add_to_cart_button")
html5_webapp_development_book.click()
basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()
time.sleep(5)
remove_first_item_btn = driver.find_element_by_class_name("remove")
remove_first_item_btn.click()
undo_btn = driver.find_element_by_link_text("Undo?")
undo_btn.click()
quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
quantity_field.clear()
quantity_field.send_keys("3")
update_basket = driver.find_element_by_name("update_cart")
update_basket.click()
quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
quantity_field_value = quantity_field.get_attribute("value")
assert quantity_field_value == '3'
time.sleep(5)
apply_coupon = driver.find_element_by_name("apply_coupon")
apply_coupon.click()
error_message = driver.find_element_by_css_selector(".woocommerce-error")
error_message_text = error_message.text
assert error_message_text == 'Please enter a coupon code.'
driver.quit()


##Shop: покупка товара##


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)

shop_tab = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
mastering_js_book = driver.find_element_by_class_name("post-165").click()
add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button ").click()
cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
proceed_to_checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))).click()
first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "billing_first_name")))
first_name.send_keys("IVAN")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("IVANOV")
email = driver.find_element_by_id("billing_email")
email.send_keys("testtteeessstttest@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("+79000000000")
country = driver.find_element_by_id("select2-chosen-1").click()
country_field = driver.find_element_by_id("s2id_autogen1_search")
country_field.send_keys("Russia")
country_field_accept = driver.find_element_by_class_name("select2-match").click()
address_street = driver.find_element_by_id("billing_address_1")
address_street.send_keys("Pushkina 1")
city = driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
country_state = driver.find_element_by_id("billing_state")
country_state.send_keys("Moscow")
postcode_zip = driver.find_element_by_id("billing_postcode")
postcode_zip.send_keys("143350")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payments = driver.find_element_by_css_selector("input[type='radio'][value='cheque']").click()
place_order = driver.find_element_by_id("place_order").click()
order_received_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//p[@class="woocommerce-thankyou-order-received"][text()="Thank you. Your order has been received."]')))
check_payments_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//tr[3]/td[text()='Check Payments']")))
driver.quit()
