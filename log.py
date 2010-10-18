#!/usr/bin/python
# -*- coding: utf8 -*-
# Description: Log read/write Class

from time import strftime

class Log():
	FileHandle = None
    
	def init(self):
		print FileHandle

	def GetDate(self):
		return str(strftime("%Y-%m-%d %H:%M:%S"))
    
	def Open(self,LogName):
		self.FileHandle = open(LogName, 'a')

	def Close(self):
		self.FileHandle.close()
    
	def Write(self, Message):
		self.FileHandle.write(str(self.GetDate())+"\t"+str(Message)+"\n")

object = Log()
object.Open("/home/alter/git/wp-uniqip/test.log")
object.Write("TEST MESSAGE")
object.Close()
