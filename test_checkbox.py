# Write a script that will open the online store: https://casenik.com.ua,
# will go to any product category and select the following check boxes - https://prnt.sc/mJSvte_N_Gpb.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_select_checkboxes():
    try:
        print("Browser start!")
        driver.get("https://casenik.com.ua")
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@href='category/Chehly']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//label[text()='Xiaomi                ']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//label[text()='10 - 20                ']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//label[text()='Есть в наличии                ']").click()
        time.sleep(3)
    finally:
        driver.quit()
        print("Browser quit!")
