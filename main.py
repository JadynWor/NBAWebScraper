import requests
import os
import shutil
import beautifulsoup

#range of years
years = list(range(1994,2023))

#url for scraping awards for mvp
url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

for year in years:   
    urls = url_start.format(year) 
    data = requests.get(urls)   #request data from url link and downloads it
    
#with open("https://docs.google.com/spreadsheets/d/1v3ktcLxITU-y2ecOpeSrgCCZH-2Jof0tTkw6YeuVL0c/edit#gid=0"):
with open("mvp/1991.html") as f: