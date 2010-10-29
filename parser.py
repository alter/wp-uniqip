#!/usr/bin/env python
# -*- coding: utf8 -*- 

import re
from time import strftime

class Parser():
	__FileHandle = None
	
	def Open(self,LogName):
		try:
			self.__FileHandle = open(LogName, 'r')
			return "Access log is open"
		except IOError, error:
			return str(error)

	def Close(self):
		self.__FileHandle.close()
		return "Access log is closed"

	def GetUniqIP(self):
		IPs = list()
		pattern = r"(?:(?:[\d]{1,3})\.){3}(?:[\d]{1,3})"
		IPs_re = re.compile(pattern)
		for line in self.CreateTodayLog():
			match = IPs_re.findall(line)
			for i in xrange(len(match)):
				if (self.ValidateIP(match[i]) == 0):
					IPs.append(match[i])
		return dict(map(lambda i:(i,1),IPs)).keys()

	#Within the class an additional method
	def ValidateIP(self, ip):
		Error = 0
		pattern = r"(?:[\d]{1,3})"
		pattern_re = re.compile(pattern)
		match = pattern_re.findall(ip)
		for i in xrange(len(match)):
			if (int(match[i]) > 255):
				Error += 1
		return Error

	#Within the class an additional method
	def GetDate(self):
		return str(strftime("%d/%b/%Y"))
	
	#Within the class an additional method
	def CreateTodayLog(self):
		TodayLogText = list()
		FullLogText = self.__FileHandle.readlines()
		for line in FullLogText:
			if(line.find(self.GetDate()) != -1):
				 TodayLogText.append(line)
		return TodayLogText
