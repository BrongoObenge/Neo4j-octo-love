import sys
from connection.ConfigDb import *


ConfigDb();
db = connectDb()

print "Database is connected : " + str(ConfigDb.isConnect)

if  sys.argv[0] == "create":
    importDatabaseNodes(db)
if  sys.argv[0] == "delete":
    deleteWholeDatabase(db)










