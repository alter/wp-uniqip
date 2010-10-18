#!/usr/bin/python
# -*- coding: utf8 -*-
# Description: Class for making logs

from time import strftime

class Log():
	__FileHandle = None
    
	def GetDate(self):
		return str(strftime("%Y-%m-%d %H:%M:%S"))
    
	def Open(self,LogName):
		try:
			self.__FileHandle = open(LogName, 'a+')
		except IOError, error:
			print "Can't open/create log file !!\n"+str(error)

	def Close(self):
		self.__FileHandle.close()
    
	def Write(self, Message):
		try:
			self.__FileHandle.write(str(self.GetDate())+"\t"+str(Message)+"\n")
		except IOError, error:
			print "Can't write to log file!!\n"+str(error)

