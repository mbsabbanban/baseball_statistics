#!/bin/python/

import urllib.request
import time
from datetime import date, timedelta

#Setting up a dynamic url

yesterday = date.today() - timedelta(1)
baseball_url = 'http://dailybaseballdata.com/cgi-bin/getstats.pl?date=' + yesterday.strftime(%m%d) + '&out=csv'

#Setting up the GET request to retrieve the HTML markup

req = urllib.request.Request('baseball_url')
response = urllib.request.urlopen(req)
html = response.read()

#Now I need to find some way to parse the markup and write to a text file