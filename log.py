#!/usr/bin/python
# -*- coding: utf8 -*-
# Description: Class for making logs

from time import strftime

class Log():
	__FileHandle = None
    
	def GetDate(self):
		return str(strftime("%Y-%m-%d %H:%M:%S"))
    
	def Open(self,LogName):
		self.__FileHandle = open(LogName, 'a')

	def Close(self):
		self.__FileHandle.close()
    
	def Write(self, Message):
		self.__FileHandle.write(str(self.GetDate())+"\t"+str(Message)+"\n")

