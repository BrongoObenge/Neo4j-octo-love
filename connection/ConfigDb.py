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
parser.read('../db_config.conf') #Defines Path
ConfigDb.url = parser.get('DATABASE', 'url')
ConfigDb.username = parser.get('DATABASE', 'username')
ConfigDb.password = parser.get('DATABASE', 'password')
isRead = True

def __init__(self):
       pass
    

def connectDb():
    graph_db = neo4j.GraphDatabaseService(ConfigDb.url)
   
    
    #####TEST
    #graph_db.
    
    
    #######
    ConfigDb.isConnect = True
    
    return graph_db

def createDatabase():
    pass

def deleteWholeDatabase(graph_db):
       graph_db.clear()
       
def deleteIndex(graph_db, nodeOrRelationship, nameOfIndex):
    result = False
    graph_db.delete_index(nodeOrRelationship, nameOfIndex)       
    result = True
    
    return result   
       



