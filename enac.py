from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import secret

driver = webdriver.Chrome()
driver.get("https://aurion-prod.enac.fr/faces/Login.xhtml")
driver.find_element(By.ID, "username").send_keys(secret.username)
driver.find_element(By.ID, "password").send_keys(secret.password)
driver.find_element(By.ID, "j_idt28").click()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, "Mon emploi du temps").click()
driver.implicitly_wait(100)
sleep(2)
driver.find_element(By.XPATH, "//button[@class='fc-month-button ui-button ui-state-default ui-corner-left ui-corner-right']").click()
sleep(2)
driver.find_element(By.ID, "form:j_idt121").click()


