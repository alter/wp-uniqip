#!/usr/bin/env python
# -*- coding: utf8 -*-

#import daemon
from log import Log 
from parser import Parser
from mysql import MySQL

def run():
	log = Log()
	parser = Parser()
	mysql = MySQL()
	log.Open("./wp-uniqip.log")
	log.Write("wp-uniqip is starting")
	log.Write(parser.Open("/var/log/nginx/localhost.access_log"))
	log.Write(mysql.Connect("localhost", "root", " ", "wordpress"))
	log.Write(mysql.Insert(parser.GetUniqIP()))
	log.Write(mysql.Disconnect())
	log.Write(parser.Close())
	log.Close()

#with daemon.DaemonContext():
run()

