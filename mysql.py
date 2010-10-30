#!/usr/bin/env python
# -*- coding: utf8 -*-

import MySQLdb

class MySQL():
	__hostname = None
	__username = None
	__password = None
	__database = None
	__dbHandle = None
	__dbCursor = None

	def Connect(self,hostname = "localhost" ,username = "wordpress" ,password = "wordpress" ,database = "wordpress"):
		self.__hostname = hostname
		self.__username = username
		self.__password = password
		self.__database = database
		try:
			self.__dbHandle = MySQLdb.connect(self.__hostname, self.__username, self.__password, self.__database)
			self.__dbCursor = self.__dbHandle.cursor()
			return "connected to MySQL"
		except Exception, error:
			return str(error)

	def Disconnect(self):
		self.__dbCursor.close()
		self.__dbHandle.commit()
		self.__dbHandle.close()
		return "disconnected from MySQL"


	def Insert(self, IPs):
		for IP in IPs:
			try:
				result = self.__dbCursor.execute("insert into wordpress.uniqvisitors(ip) values(\'"+str(IP)+"\')")
			except Exception, error:
				print str(error)

	def DropTable(self):
		try:
			result = self.__dbCursor.execute("DROP TABLE `uniqvisitors`;")
		except Exception, error:
			return str(error)

	def CreateTable(self):
		try:
			result = self.__dbCursor.execute("CREATE TABLE `uniqvisitors` (`id` int(11) NOT NULL auto_increment, `ip` varchar(15) NOT NULL, `date` date default NULL,PRIMARY KEY  (`id`), UNIQUE KEY `UniqIpPerDay` (`ip`,`date`)) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;")
		except Exception, error:
			return str(error)

	def DropTrigger(self):
		try:
			result = self.__dbCursor.execute("DROP TRIGGER `uniqvisitors_date_tr`;")
		except Exception, error:
			return str(error)

	def CreateTrigger(self):
		try:
			result = self.__dbCursor.execute("CREATE TRIGGER `uniqvisitors_date_tr` BEFORE INSERT ON `uniqvisitors` FOR EACH ROW set new.date = CURDATE();")
		except Exception, error:
			return str(error)
