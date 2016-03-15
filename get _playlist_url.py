from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

def start_firefox():
	profile = webdriver.FirefoxProfile("/home/tabo/.mozilla/firefox/wrhbot21.SELENIUM")
	
	return webdriver.Firefox(profile)


