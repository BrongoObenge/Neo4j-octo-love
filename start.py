import sys
from connection.ConfigDb import *


ConfigDb();
db = connectDb()

print "Database is connected : " + str(ConfigDb.isConnect)

if  sys.argv[0] == "create":
    createDatabase(db)
if  sys.argv[0] == "delete":
    sure = raw_input("You are about to DELETE the whole database\nAre you sure? y/n")
    if sure == "y":
        deleteWholeDatabase(db)
    else: pass









