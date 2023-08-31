from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import secret

driver = webdriver.Chrome()
driver.get("https://aurion-prod.enac.fr/faces/Login.xhtml")
driver.find_element(By.ID, "username").send_keys(secret.username)
driver.find_element(By.ID, "password").send_keys(secret.password)
driver.find_element(By.XPATH, "//div[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right']").click()
sleep(0.5)
driver.find_element(By.XPATH, "//li[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all ui-state-highlight']").click()
driver.find_element(By.ID, "j_idt28").click()
driver.implicitly_wait(10)
sleep(2)
driver.find_element(By.LINK_TEXT, "Mon emploi du temps").click()
driver.implicitly_wait(100)
sleep(2)
driver.find_element(By.XPATH, "//button[@class='fc-month-button ui-button ui-state-default ui-corner-left ui-corner-right']").click()
sleep(2)
driver.find_element(By.ID, "form:j_idt121").click()
sleep(2)
driver.find_element(By.XPATH, '//body').send_keys(Keys.CONTROL + Keys.HOME)
sleep(2)
driver.find_element(By.XPATH, "//button[@class='fc-next-button ui-button ui-state-default ui-corner-left ui-corner-right']").click()
sleep(2)
driver.find_element(By.ID, "form:j_idt121").click()



