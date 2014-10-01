'''
Created on 1 Oct 2014

@author: j
'''
from ConfigParser import SafeConfigParser

class ConfigDb:
    url = None
    username = None
    password = None
#Get Data from db_config.conf   
parser = SafeConfigParser()
parser.read('../db_config.conf') #Defines Path
    
ConfigDb.url = parser.get('DATABASE', 'url')
ConfigDb.username = parser.get('DATABASE', 'username')
ConfigDb.password = parser.get('DATABASE', 'password')
    


