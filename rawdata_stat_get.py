#!/bin/python/

import urllib.request
import time
from datetime import date, timedelta
from bs4 import BeautifulSoup
import re
import pymysql
import csv


##### DECLARING GLOBAL VARIABLES #####
#yesterday = date.today() - timedelta(1)

#For doing a data backfill, need to adjust the yesterday date
yesterday = date(2014,4,30)
#print (yesterday.strftime("%m%d"))


###### Function for getting raw daily baseball data #####

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
	clean_html_with_date = clean_html.replace('\n',','+yesterday.strftime("%y-%m-%d")+'\n')
	clean_html_with_date = clean_html_with_date + ','+yesterday.strftime("%y-%m-%d")
	
	print("Fetching raw data from the website")
	print("...")
	print(clean_html_with_date)

	#print(clean_html)

	#I am creating a test .csv file and then writing to it using open(),write(),close()

	f = open("baseball_rawdata.csv", "w")
	f.write(clean_html_with_date)
	f.close()

##### END OF getBaseballData FUNCTION #####


##### Function for inserting raw baseball data into mysql database #####

#DATABASE insert should probably be declared in a new function
#http://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python
#https://github.com/PyMySQL/PyMySQL/blob/master/example.py

#Will probably end up using pymysql for my python3 and mysql connector

def pymysqlRawDataInsert():
	
	#localhost connection
	#conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='baseball_stats')
	conn = pymysql.connect(host='69.195.124.91', port=3306, user='mattsabb_bsball', passwd='letsgomets', db='mattsabb_baseball')
	cur = conn.cursor()
	
	z = open("insert.txt", "w")
	print("...")
	print("Inserting data into the database")
	
	
	with open('baseball_rawdata.csv', 'r') as csvfile:
		csv_data = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		#print(csv_data)
		#empty_row = [""]
		#print(empty_row)
		#print(len(empty_row))
		
		#Declaring all the variables
		
		mlb_id = ''
		name = ''
		team = ''
		game = ''
		game_no = ''
		result = ''
		hitter_pitcher = ''
		starter = ''
	#	ab = ''
	#	h = ''
	#	dbl = ''
	#	trp = ''
	#	hr = ''
	#	r = ''
	#	rbi = ''
	#	bb = ''
	#	ibb = ''
	#	hbp = ''
	#	so = ''
	#	sb = ''
	#	cs = ''
	#	sh = ''
	#	sf = ''
	#	e = ''
	#	pb = ''
	#	lob = ''
	#	gidp = ''
	#	ip = ''
	#	ha = ''
	#	ra = ''
	#	er = ''
	#	wk = ''
	#	iwk = ''
	#	k = ''
	#	hb = ''
	#	pickoffs = ''
	#	wp = ''
	#	win = ''
	#	loss = ''
	#	save = ''
	#	bs = ''
	#	hold = ''
		position = ''
	#	cg = ''
		hit_date = ''
		
		for row in csv_data:

			mlb_id = row[0]
			name = row[1].replace("'","")
			team = row[2]
			game = row[3]
			game_no = row[4]
			result = row[5]
			hitter_pitcher = row[6]
			starter = row[7]
			ab = int(row[8]) if row[8] else 0
			h = int(row[9]) if row[9] else 0
			
			dbl = int(row[10]) if row[10] else 0
			trp = int(row[11]) if row[11] else 0
			hr = int(row[12]) if row[12] else 0
			r = int(row[13]) if row[13] else 0
			rbi = int(row[14]) if row[14] else 0
			bb = int(row[15]) if row[15] else 0
			ibb = int(row[16]) if row[16] else 0
			hbp = int(row[17]) if row[17] else 0
			so = int(row[18]) if row[18] else 0
			sb = int(row[19]) if row[19] else 0
			cs = int(row[20]) if row[20] else 0
			
			picked_off = int(row[21]) if row[21] else 0
			sh = int(row[22]) if row[22] else 0
			sf = int(row[23]) if row[23] else 0
			e = int(row[24]) if row[24] else 0
			pb = int(row[25]) if row[25] else 0
			lob = int(row[26]) if row[26] else 0
			gidp = int(row[27]) if row[27] else 0
			ip = float(row[28]) if row[28] else 0.0
			ha = int(row[29]) if row[29] else 0
			ra = int(row[30]) if row[30] else 0
			
			er = int(row[31]) if row[31] else 0
			wk = int(row[32]) if row[32] else 0
			iwk = int(row[33]) if row[33] else 0
			k = int(row[34]) if row[34] else 0
			hb = int(row[35]) if row[35] else 0
			pickoffs = int(row[36]) if row[36] else 0
			hr_allowed = int(row[37]) if row[37] else 0
			wp = int(row[38]) if row[38] else 0
			win = int(row[39]) if row[39] else 0
			loss = int(row[40]) if row[40] else 0
			
			save = int(row[41]) if row[41] else 0
			bs = int(row[42]) if row[42] else 0
			hold = int(row[43]) if row[43] else 0
			position = row[44]
			cg = int(row[45]) if row[45] else 0
			hit_date = yesterday.strftime("%y-%m-%d")
			
		#	print (row)
		#	print (h)
		#	print (position)
		#	print (mlb_id, name, team, game)
			
		#	query_string = str(row).strip('[]')
		#	print(query_string)
		
		
		# Localhost Collections
		
		#	insert_query = """INSERT INTO baseball_stats.raw_baseball_data (MLB_ID, NAME, TEAM, GAME, GAME_NO, RESULT, HITTER_PITCHER, STARTER, AB, H, 2B, 3B, HR, R, RBI, BB, IBB, HBP, SO, SB, CS, PICKED_OFF, SH, SF, E, PB, LOB, GIDP, IP, HA, RA, ER, WK, IWK, K, HB, PICKOFFS, HR_ALLOWED, WP, WIN, LOSS, SAVE, BS, HOLD, POSITION, CG, HIT_DATE) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (mlb_id, name, team, game, game_no, result, hitter_pitcher, starter, ab, h, dbl, trp, hr, r, rbi, bb, ibb, hbp, so, sb, cs, picked_off, sh, sf, e, pb, lob, gidp, ip, ha, ra, er, wk, iwk, k, hb, pickoffs, hr_allowed, wp, win, loss, save, bs, hold, position, cg, hit_date)
			
			insert_query = """INSERT INTO mattsabb_baseball.raw_baseball_data (MLB_ID, NAME, TEAM, GAME, GAME_NO, RESULT, HITTER_PITCHER, STARTER, AB, H, 2B, 3B, HR, R, RBI, BB, IBB, HBP, SO, SB, CS, PICKED_OFF, SH, SF, E, PB, LOB, GIDP, IP, HA, RA, ER, WK, IWK, K, HB, PICKOFFS, HR_ALLOWED, WP, WIN, LOSS, SAVE, BS, HOLD, POSITION, CG, HIT_DATE) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (mlb_id, name, team, game, game_no, result, hitter_pitcher, starter, ab, h, dbl, trp, hr, r, rbi, bb, ibb, hbp, so, sb, cs, picked_off, sh, sf, e, pb, lob, gidp, ip, ha, ra, er, wk, iwk, k, hb, pickoffs, hr_allowed, wp, win, loss, save, bs, hold, position, cg, hit_date)
			
			print (("Writing to db : %s") % insert_query)
		

		#Executing the SQL statements
		
			cur.execute(insert_query)
		#	cur.execute("SELECT * from mattsabb_baseball.raw_baseball_data;")

		#Writing results to test file
		
			z.write(insert_query)
			z.write("\n")
		
		print ( "Data has been inserted into the table" )	
		z.close()

	#print(cur.fetchall())
	#print(cur.description)
	
	conn.commit()
	cur.close()
	conn.close()

##### END OF pymysqlRawDataInsert FUNCTION #####
	
##### RUNNING THE FUNCTIONS TO GENERATE REPORT #####

getBaseballData()
pymysqlRawDataInsert()