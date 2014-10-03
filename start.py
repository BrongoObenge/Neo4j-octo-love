#!/usr/bin/env python
import sys
from connection.ConfigDb import *


ConfigDb()
print "Connecting to database!"
db = connectDb()
help = "Usage ./start.py [Command]\n" \
       "\tcreate : Creates the Nodes and Relationships.\n" \
       "\tdelete : Deleletes the entire database.\n" \
       "\thelp : Prints this window."

print "Database is connected : " + str(ConfigDb.isConnect)

#takes commands from commandline
if  sys.argv[1] == "create":
    createDatabase(db)
if  sys.argv[1] == "delete":
    deleteWholeDatabase(db)
if sys.argv[1] == "help":
    print help









