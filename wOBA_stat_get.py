#!/bin/python/

import urllib.request
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import re

#Global Variables
yesterday = date.today() - timedelta(1)

#Function for getting raw daily baseball data

#Setting up a dynamic url

baseball_url = 'http://dailybaseballdata.com/cgi-bin/getstats.pl?date=' + yesterday.strftime("%m%d") + '&out=csv'

print(baseball_url)

#Setting up the GET request to retrieve the HTML markup

req = urllib.request.Request(baseball_url)
response = urllib.request.urlopen(req)
html = response.read()

#Using BeautifulSoup to parse the markup for info, removing script and other unnecessary tags

clean_html = BeautifulSoup(html)
to_extract = clean_html.findAll('script')

for item in to_extract:
	item.extract()

clean_html = clean_html.get_text()
clean_html = clean_html.strip() #strip removes all the whitespace
clean_html = '\n'.join(clean_html.split('\n')[5:]) #Slice at the end removes the first 5 lines and then joining together by '\n'

print(clean_html)

#I am creating a test file and then writing to it using open(),write(),close()

f = open("test.txt", "w")
f.write(clean_html)
f.close()

#DATABASE insert should probably be declared in a new function
#http://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python)