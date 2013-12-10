#!/usr/bin/env python
# encoding=utf8

"""

SYNOPSIS

DESCRIPTION

EXAMPLES

AUTHOR

LICENSE

VERSION  

"""

import MySQLdb as mysql

DB_HOST = 'localhost'
DB_NAME = 'information_schema'
DB_PORT = 3306
DB_USER = 'root'
DB_PASS = 'root'

con = mysql.connect(host=DB_HOST, db=DB_NAME, user=DB_USER, passwd=DB_PASS, port=DB_PORT)