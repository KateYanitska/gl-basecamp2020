#task 2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.globallogic.com/ua/careers/")

driver.find_element_by_name("keywords").send_keys("QA" + Keys.RETURN)

first_result = wait.until(presence_of_element_located((By.CLASS_NAME, "mb-0")))
print(first_result.get_attribute("textContent"))

#driver.close()
