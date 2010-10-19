#!/usr/bin/python
# -*- coding: utf8 -*-

import MySQLdb

class MySQL():
	hostname = "localhost"
	username = "wordpress"
	password = "wordpress"
	database = "wordpress"
	__dbHandle = None

	def init(hostname,username,password,database):
		self.hostname = hostname
		self.username = username
		self.password = password
		self.database = database

	def Connect(self):
		try:
			self.__dbHandle = MySQLdb.connect(hostname,username,password,database)
			return dbHandle
		except IOError, error
			return str(error)

	def Disconnect(self):
		self.__dbHandle.close()

	def Insert(self, IPs):
		cursor = self.__dbHandle.cursor()
		for IP in IPs:
			try:
				result = cursor.execute("insert into wordpress.uniqvisitors(ip) values(\'"+str(IP)+"\')")
			except Exception, error:
				return error

