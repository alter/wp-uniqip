#!/usr/bin/python
# -*- coding: utf8 -*- 
# version 0.0.1_alpha

import sys
import MySQLdb
import time
import datetime

def ReadApacheLog(LogName):
	try:
		LogFile = open(LogName)
		LogText = LogFile.readlines()
		LogFile.close()
		return LogText
	except IOError, err:
		print IOError, err
		return 1

def ParseApacheLog(LogText):
	IPList = list()
	for i in range(len(LogText)):
		IPList.append(LogText[i].split()[0])
	return UniqIPList(IPList)

def UniqIPList(IPList):
	return dict(map(lambda i:(i,1),IPList)).keys()

def MysqlConnect():
	db = MySQLdb.connect(host='localhost', user='wordpress', passwd='wordportal', db='wordpress')
	return db

def MysqlExec(db, UniqIP):
	cursor = db.cursor()
	for ip in UniqIP:
		try:
                	result = cursor.execute("insert into wordpress.uniqvisitors(ip) values(\'"+str(ip)+"\')")
        	except Exception, err:
                	ParserLogFile(ip, err)

def ParserLogFile(ip, err):
	ParserLog = open("/var/log/parser.log",'a')
	today = datetime.date.today()
	ParserLog.write("DATE: "+str(today)+"\nIP: "+str(ip)+ "\nMessage: "+str(err)+"\n\n")
	ParserLog.close()
	return
	

def CurDate():
	today = datetime.date.today()
	return today.strftime("%d/%B")[:6]
	

def main():
	ParserLogFile("127.0.0.1","[ Parser.py starting ]")
	LogName = "/var/log/apache2/domain.nam_log"
	MysqlConnect()
	LogText = ReadApacheLog(LogName)
	MysqlExec(MysqlConnect(),ParseApacheLog(LogText))

if __name__ == '__main__':
	main()
