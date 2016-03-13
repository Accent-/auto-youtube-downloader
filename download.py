from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# url = ["https://www.youtube.com/watch?v=y6EYV2yPY98&list=PL12qDA9vz7yqvz3pfXZOTbVqukYgEyXQB", "https://www.youtube.com/watch?v=G07coU1GnYc&index=2&list=PL12qDA9vz7yqvz3pfXZOTbVqukYgEyXQB"]


profile = webdriver.FirefoxProfile("/home/tabo/.mozilla/firefox/wrhbot21.SELENIUM")
driver = webdriver.Firefox(profile)

driver.get("http://offliberty.com/")


driver.find_element_by_name("track").send_keys(url)
driver.find_element_by_name("submit").click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "video_file")))
driver.find_element_by_id("video_file").click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "download")))
t = driver.find_elements_by_class_name("download")
t[1].click()

driver.close()

