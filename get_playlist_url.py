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

urls = ["https://www.youtube.com/watch?v=2eGazzxcp3I&list=PLKKGuVlUwpxD2XaRfSJx6Y9jX-fqR7FOc&index=1",
		"https://www.youtube.com/watch?v=IM_uUYGHQGo&list=PLKKGuVlUwpxD2XaRfSJx6Y9jX-fqR7FOc&index=200",
		"https://www.youtube.com/watch?v=rh517TMtVbo&list=PLKKGuVlUwpxD2XaRfSJx6Y9jX-fqR7FOc&index=398",
		"https://www.youtube.com/watch?v=OCGIWbAD9RQ&index=596&list=PLKKGuVlUwpxD2XaRfSJx6Y9jX-fqR7FOc"]

video_link = []

for url in urls:
	driver.get(url)


	html = urlopen(driver.current_url)

	# html = open("./youtube_playlist.html")

	bsObj = BeautifulSoup(html.read(), "html.parser")

	
	for link in bsObj.find_all('a'):
		if "list=PLKKGuVlUwpxD2XaRfSJx6Y9jX-fqR7FOc" in link.get("href"):
			video_link.append("https://www.youtube.com/" + link.get('href'))

	video_link = list(set(video_link))

	# print(video_link)
	print(len(video_link))


video_link = [x + "\n" for x in video_link]

with open("youtube_list.txt", 'w') as f:
	f.writelines(video_link)


