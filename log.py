#!/usr/bin/env python
# -*- coding: utf8 -*-

from time import strftime

class Log():
	__FileHandle = None

    
	def GetDate(self):
		return str(strftime("%Y-%m-%d %H:%M:%S"))
    
	def Open(self,LogName):
		try:
			self.__FileHandle = open(LogName, 'a+')
			self.Write("wp-uniqip.log open")
		except IOError, error:
			print "Can't open/create log file !!\n"+str(error)

	def Close(self):
		self.Write("wp-uniqip.log is closed")
		self.__FileHandle.close()
    
	def Write(self, Message):
		try:
			self.__FileHandle.write(str(self.GetDate())+"\t"+str(Message)+"\n")
		except IOError, error:
			print "Can't write to log file!!\n"+str(error)

