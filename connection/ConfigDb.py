#!/usr/bin/python
'''
Created on 1 Oct 2014

@author: j
'''
from ConfigParser import SafeConfigParser
from py2neo import *

class ConfigDb:
    'Configure database. Add Delete Modify'
    url = None
    username = None
    password = None
    isRead = False
    isConnect = False

#Get Data from db_config.conf
parser = SafeConfigParser()
#TODO add an exception
parser.read('db_config.conf') #Defines Path

ConfigDb.url = parser.get('DATABASE', 'url')
ConfigDb.username = parser.get('DATABASE', 'username')
ConfigDb.password = parser.get('DATABASE', 'password')
isRead = True

def __init__(self):
       pass
    

def connectDb():
    graph_db = neo4j.GraphDatabaseService(ConfigDb.url)
    ConfigDb.isConnect = True
    return graph_db

def createDatabase(graph_db):
    importDatabaseNodes(graph_db)



def deleteWholeDatabase(graph_db):
       print "Preparing to delete database"
       graph_db.clear()
       print "Success!"
       
def deleteIndex(graph_db, nodeOrRelationship, nameOfIndex):
    result = False
    graph_db.delete_index(nodeOrRelationship, nameOfIndex)       
    result = True
    
    return result   
       
def importDatabaseNodes(graph_db):

    print "Opening file . . ."
    try:
        file = "create_db"
        dbFile=open(file,'r')
    except:
        print "Error while loading file"
        return "Error!"
    
    print "File " + dbFile.name + " opened! " + "\nin the mode : " + dbFile.mode
    print "Creating Nodes..."
       
    for line in dbFile.readlines():
        graph_db.create(eval(line))
    print "Success creating nodes!"

def importDatabaseRelations(graph_db):
    try:
        file = "create_rel"
        dbFile=open(file,'r')
    except:
        print "Error while loading file"
        return "Error!"
    for line in dbFile.readlines():
        neo4j.CypherQuery(graph_db, eval(line))

def openQueryTransaction():
    session = cypher.Session(ConfigDb.url)
    tx = session.create_transaction()
    return tx
