import sys
from connection.ConfigDb import *


ConfigDb();
db = connectDb()

print "Database is connected : " + str(ConfigDb.isConnect)

if  sys.argv[1] == "create":
    importDatabaseNodes(db)


if  sys.argv[1] == "delete":
    deleteWholeDatabase(db)










