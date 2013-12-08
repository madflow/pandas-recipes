#!/usr/bin/env python

"""

SYNOPSIS

DESCRIPTION

EXAMPLES

AUTHOR

LICENSE

VERSION  

"""

import pandas as pd
import numpy as np
import pandas.io.sql as psql
import MySQLdb as mysql

DB_HOST = 'localhost'
DB_NAME = 'dbname'
DB_PORT = 3306
DB_USER = ''
DB_PASS = ''

con = mysql.connect(host=DB_HOST, db=DB_NAME, user=DB_USER, passwd=DB_PASS, port=DB_PORT)