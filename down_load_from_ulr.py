from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

def start_firefox():
	profile = webdriver.FirefoxProfile("/home/tabo/.mozilla/firefox/wrhbot21.SELENIUM")
	
	return webdriver.Firefox(profile)





driver = start_firefox()

for url in video_link:
	driver.get("http://offliberty.com/")
	time.sleep(random.randint(2, 7))

	driver.find_element_by_name("track").send_keys(url)
	driver.find_element_by_name("submit").click()
	try:
		WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "video_file")))
		time.sleep(random.randint(5, 9))
		driver.find_element_by_id("video_file").click()
		WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "download")))
		time.sleep(random.randint(7, 10))
		
		t = driver.find_elements_by_class_name("download")
		t[1].click()
		time.sleep(random.randint(3, 7))

	except:
		with open("dl.log", 'a') as f:
			f.write(url)

		continue	

driver.close()