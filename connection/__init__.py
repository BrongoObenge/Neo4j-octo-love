'''
Connection Neo4j


'''
from py2neo import *
from Config import *

class Connection:
    configurl = ConfigDb()

    url = configurl.url # Gets the database url from the config file
    graph_db = neo4j.GraphDatabaseService(url)
    
    











