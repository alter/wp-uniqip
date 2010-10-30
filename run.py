#!/usr/bin/env python
# -*- coding: utf8 -*-

from Daemon import Daemon 
from log import Log 
from parser import Parser
from mysql import MySQL
from optparse import OptionParser
import sys,time

class UniqIP(Daemon):
	logpath			=	"/tmp/wp-uniqip.log"						# log path
	accesslogpath	=	"/var/log/nginx/localhost.access_log"		# access log path (apache,nginx,lighttpd, etc...) 
	mysql_hostname	=	"localhost"									# mysql host name
	mysql_username	=	"root"										# mysql user name
	mysql_password	=	" "											# mysql user password
	mysql_database	=	"wordpress"									# mysql database name

	log = Log()
	parser = Parser()
	mysql = MySQL()

	def run(self):
		while True:
			print	self.log.Open(self.logpath)
			print	self.log.Write(self.parser.Open(self.accesslogpath))
			print	self.log.Write(self.mysql.Connect(self.mysql_hostname, self.mysql_username, self.mysql_password, self.mysql_database))
			print	self.log.Write(self.mysql.Insert(self.parser.GetUniqIP()))
			print	self.log.Write(self.mysql.Disconnect())
			print	self.log.Write(self.parser.Close())
			print	self.log.Close()
			print	time.sleep(60*15) 								# 15 minutes
	
	def install(self):
		print self.mysql.Connect(self.mysql_hostname, self.mysql_username, self.mysql_password, self.mysql_database)
		self.mysql.DropTable()
		self.mysql.DropTrigger()
		self.mysql.CreateTable()
		self.mysql.CreateTrigger()
		print self.mysql.Disconnect()

if __name__ == "__main__":
	daemon = UniqIP('/tmp/wp-uniqip.pid')                   # pid path(better to change path to /var/run/wp-uniqip.pid)
	usage = "\t./%prog [options]"
	parser = OptionParser(usage=usage)
	parser.add_option("-i", "--install", action="store_true", dest="install", default="False", help="install table and trigger to db")
	options,args = parser.parse_args()
	if (options.install == True):
		daemon.install()
	else:
		if (len(sys.argv) == 2):
			if 'start' == sys.argv[1]:
				daemon.start()
			elif 'restart' == sys.argv[1]:
				daemon.restart()
			elif 'stop' == sys.argv[1]:
				daemon.stop()
			else:
				print "Unknown command\n USE start|restart|stop\n"
				sys.exit(2)
			sys.exit(0)
		else:
			print "Usage: %s start|restart|stop" % sys.argv[0]
			sys.exit(2)

