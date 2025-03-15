# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.find_element(By.ID, "user-name").send_keys("visual_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()
# driver.maximize_window()
# time.sleep(5)
#
# driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
# driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
# driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
# driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
# driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
# driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
# logout_button = driver.find_element(By.ID, "logout_sidebar_link")
# driver.execute_script("arguments[0].click();", logout_button)
# driver.find_element(By.ID, "logout_sidebar_link").click()
# time.sleep(5)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("visual_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(3)

menu_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
)
menu_button.click()
time.sleep(2)  # Wait for the menu to open

# Wait for the logout button to appear
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
)

# Click the logout button
logout_button.click()

# Wait and close the browser
time.sleep(5)
driver.quit()








