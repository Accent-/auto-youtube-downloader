import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

# url test
html = urlopen("https://www.youtube.com/playlist?list=PLUav54rc5MQAJpXKjiRDbbTW_uVX1Fl2B")

# html = open("./youtube_playlist.html")

bsObj = BeautifulSoup(html.read(), "html.parser")

video_link = []

for link in bsObj.find_all('a'):
	if "/watch" in link.get("href"):
		video_link.append("https://www.youtube.com/" + link.get('href'))

video_link = list(set(video_link))

print(video_link)
print(len(video_link))

# file open test
# video = []
# with open("./youtube_list.txt", 'r') as f:
# 	for l in f:
# 		video.append(l.replace("\n", ""))

