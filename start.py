import sys
from connection.ConfigDb import ConfigDb


ConfigDb();
#db = connectDb()

print "Database is connected : " + str(ConfigDb.isConnect)

if  sys.argv[1] == "create":
    ConfigDb()#importDatabaseNodes(db)


if  sys.argv[1] == "delete":
    ConfigDb()#deleteWholeDatabase(db)










