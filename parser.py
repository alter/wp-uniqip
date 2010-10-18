#!/usr/bin/python
# -*- coding: utf8 -*- 
# Description: Class Parser must return list of uniq ips
# per day from access log of web server

import re
from time import strftime

class Parser():
	__FileHandle = None
	
	def Open(self,LogName):
		self.__FileHandle = open(LogName, 'r')

	def Close(self):
		self.__FileHandle.close()

	def GetUniqIP(self):
		IPs = list()
		for line in self.__FileHandle:
			IPs += re.findall('(?:(?:[\d]{1,3})\.){3}(?:[\d]{1,3})', line)
		return dict(map(lambda i:(i,1),IPs)).keys()

	def GetDate(self):
		return str(strftime("%d/%b/%Y"))

	def CreateTodayLog(self):
		for line in self.__FileHandle:
			

obj = Parser()
print obj.GetDate()
#obj.Open("/var/log/auth.log")
#print obj.GetUniqIP()
#obj.Close()
