#!/usr/bin/python
'''
Connection Neo4j


'''
from ConfigDb import *


class Connection: pass
    
ConfigDb();
db = connectDb()
print "Database is connected : " + str(ConfigDb.isConnect)


#importDatabaseNodes(db)
deleteWholeDatabase(db)





















