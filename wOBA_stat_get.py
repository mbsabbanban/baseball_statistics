#!/bin/python/

import urllib.request
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import re
import pymysql
import csv


##### DECLARING GLOBAL VARIABLES #####
yesterday = date.today() - timedelta(1)

#Function for getting raw daily baseball data
def getBaseballData():

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
	clean_html = '\n'.join(clean_html.split('\n')[6:]) #Slice at the end removes the first 5 lines and then joining together by '\n'
	clean_html_with_date = clean_html.replace('\n',yesterday.strftime("%y-%m-%d")+'\n')
	clean_html_with_date = clean_html_with_date + yesterday.strftime("%y-%m-%d")
	
	print(clean_html_with_date)

	#print(clean_html)

	#I am creating a test .csv file and then writing to it using open(),write(),close()

	f = open("test.csv", "w")
	f.write(clean_html_with_date)
	f.close()

##### END OF getBaseballData FUNCTION #####


#DATABASE insert should probably be declared in a new function
#http://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python
#https://github.com/PyMySQL/PyMySQL/blob/master/example.py

#Will probably end up using pymysql for my python3 and mysql connector

def pymysqlTest(): #Test function of pymysql just to pull data
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='baseball_stats')
	cur = conn.cursor()
	
	with open('test.csv', 'r') as csvfile:
		csv_data = csv.reader(csvfile, delimiter='|', quotechar='|')
		for row in csv_data:
		#	print(', '.join(row))
			print(row)
		#	cur.execute("SELECT * from baseball_stats.raw_baseball_data;")
			cur.execute('INSERT INTO baseball_stats.raw_baseball_data (MLB_ID, NAME, TEAM, GAME, GAME_NO, RESULT, HITTER_PITCHER, STARTER, AB, H, 2B, 3B, HR, R, RBI, BB, IBB, HBP, SO, SB, CS, SH, SF, E, PB, LOB, GIDP, IP, HA, RA, ER, WK, IWK, K, HB, PICKOFFS, WP, WIN, LOSS, SAVE, BS, HOLD, POSITION, CG, HIT_DATE)' 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)

	#print(cur.description)
	#print()
		
	cur.close()
	conn.close()

##### RUNNING THE FUNCTIONS TO GENERATE REPORT $$$$$

#getBaseballData()
pymysqlTest()