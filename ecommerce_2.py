from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("[class='search-keyword']").send_keys("ber")
time.sleep(5)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

"""Adding products to the card and proceeding to the checkout page"""
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

"""Entering the promocode and clicking on the 'Apply Button' """
Promocode = driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

time.sleep(5)
print(driver.find_element_by_css_selector("span.promoInfo").text)

