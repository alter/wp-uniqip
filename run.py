#!/usr/bin/env python
# -*- coding: utf8 -*-

from Daemon import Daemon 
from log import Log 
from parser import Parser
from mysql import MySQL
import sys,time

class UniqIP(Daemon):

	def run(self):
		while True:
			log = Log()
			parser = Parser()
			mysql = MySQL()
			log.Open("/home/alter/git/wp-uniqip/log.log") 					# log path
			log.Write(parser.Open("/var/log/nginx/localhost.access_log")) 	# access log path (apache,nginx,lighttpd, etc...)
			log.Write(mysql.Connect("localhost", "root", " ", "wordpress"))	# hostname, username, password, database for mysql
			log.Write(mysql.Insert(parser.GetUniqIP()))
			log.Write(mysql.Disconnect())
			log.Write(parser.Close())
			log.Close()
			time.sleep(60*15) 												# 15 minutes


if __name__ == "__main__":
	daemon = UniqIP('/tmp/wp-uniqip.pid')									# pid path(better to change path to /var/run/wp-uniqip.pid)
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
		print "usage: %s start|restart|stop" % sys.argv[0]
		sys.exit(2)

