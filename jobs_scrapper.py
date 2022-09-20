import urllib.request
from bs4 import BeautifulSoup

url = "https://www.seek.com.au/software-engineer-jobs"

request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read(by)