#!/bin/python/

import urllib.request
import time
from datetime import date, timedelta

#Setting up a dynamic url

yesterday = date.today() - timedelta(1)
baseball_url = 'http://dailybaseballdata.com/cgi-bin/getstats.pl?date=' + yesterday.strftime("%m%d") + '&out=csv'

print(baseball_url)

#Setting up the GET request to retrieve the HTML markup

req = urllib.request.Request(baseball_url)
response = urllib.request.urlopen(req)
html = response.read()

print(html)

###Now I need to find some way to parse the markup and write to a text file

#This is where I'm going to parse the markup for the information that I need and then save it to the variable

#I am creating a test file and then writing to it using open(),write(),close()

f = open("test.txt", "wb")
f.write(html)
f.close()

#Still need to find some way to get rid of unnecessary HTML, just need the document itself...