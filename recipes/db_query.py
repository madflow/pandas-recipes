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

import pandas.io.sql as pysql
from db_mysql import con

df = pysql.frame_query('SELECT * FROM PLUGINS', con)

print df.head(1)

