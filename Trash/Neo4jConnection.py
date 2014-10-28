'''
Created on 1 Oct 2014

@author: j
'''
from py2neo import neo4j
from ConfigParser import SafeConfigParser


class Neo4jConnection:
    isConnected = False
    

def __init__(self):
    pass
    
def connectDatabase():
    url = getUrl()
    graph_db = neo4j.GraphDatabaseService(url)
    Neo4jConnection.isConnected = True
    return graph_db 

def getUrl():
    parser = SafeConfigParser()
    parser.read('../db_config.conf')
    
    url = parser.get('DATABASE', 'url')
    username = parser.get('DATABASE', 'username')
    password = parser.get('DATABASE', 'password')

    return url, username, password

def debug():
    pass


