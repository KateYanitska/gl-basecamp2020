#task 1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
assert "Google" in driver.title
search_field = driver.find_element_by_name("q")
search_field.send_keys("selenium install ubuntu python")
search_field.send_keys(Keys.RETURN)
link = driver.find_element_by_partial_link_text("pypi.org")
link.click()
pypi_search_field = driver.find_element_by_name("q")
pypi_search_field.send_keys("selenium")
pypi_search_field.send_keys(Keys.RETURN)
second_link = driver.find_element_by_xpath("//ul/li[2]/a/h3")
second_link.click()

#driver.close()
