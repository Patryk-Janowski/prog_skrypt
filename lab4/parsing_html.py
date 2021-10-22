#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup
import requests

# response = requests.get("https://google.com/")
# if response.status_code != 200:
# 	print("Error fetching page")
# 	exit()
# else:
# 	content = response.content

with open('polak.icsr.agh.edu.html', 'r') as f:
    content = f.read()

print(re.findall(r'<!--.*?-->', content))
