#!/usr/bin/python
'''
Connection Neo4j


'''
from py2neo import *
from ConfigDb import *
from Parse import *

class Connection: pass
    
ConfigDb();
db = connectDb()
print "Database is connected : " + parseBoolean(ConfigDb.isConnect)   











