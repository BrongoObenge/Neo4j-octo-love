#!/usr/bin/env python
import sys
from connection.ConfigDb import *


ConfigDb()
db = connectDb()

print "Database is connected : " + str(ConfigDb.isConnect)

#takes commands from commandline
if  sys.argv[1] == "create":
    createDatabase(db)
if  sys.argv[1] == "delete":
    deleteWholeDatabase(db)









