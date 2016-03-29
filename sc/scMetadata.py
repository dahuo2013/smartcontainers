# Metadata functions
# Metadata should 

from sarge import Command, Capture, get_stdout, get_stderr, capture_stdout
import provinator
import sc
import os
import re
import ast
from rdflib import Literal, BNode, Namespace, URIRef, Graph, Dataset, RDF, RDFS, XSD
from rdflib.namespace import FOAF
from rdflib.serializer import Serializer
import rdflib.resource
import uuid

class scMetadata:
    def __init__(self):
        #initial scMetadata

        self.ldpcontainerlist = {}

    def initialNamespace(self):
    	pass

    def createLDPContainer(self, url, namespace):
    	#create LDP Container
    	#docker create file folder
    	#docker create file
    	#append LDP Container meta
    	if namespace not in self.ldpcontainerlist and url not in self.ldpcontainerlist.itervalues():
    		
    		self.ldpcontainerlist[namespace] = url
    		print self.ldpcontainerlist
    		self.dockerCreateFolder(url, namespace)
    	else:
    		print "error, key or value already exsits"


    def dockerCreateFolder(self, url, namespace):
    	if not os.path.exists(url):
    		os.makedirs(url+namespace)
    		file = open(url+namespace+"/.meta", 'w+')
    		file.close()
    	print url+namespace
    	print url+namespace+"/.meta"

    	

    def createLDPResource(self, url):
    	#create LDP Resources
    	#docker create file
    	#append LDP Container meta
    	pass

    def appendData(self, filepath):
        #Appends provinator data to the file passed in
        with open(filepath, 'a') as provfile:
            provfile.write(provinator.get_commit_data())

    def labelDictionary(self,label_prefix):
        #Returns the label as a dictionary
        #Get the label information from provinator
        provOutput = provinator.get_commit_label()
        #Remove any formatting characters
        provOutput = re.sub('[\t\r\n\s+]', '', provOutput)
        #Add the label prefix
        newLabel =  "{'" + label_prefix + "':'" + provOutput + "'}"
        #Evaluate the string to create the dictionary
        newLabel = ast.literal_eval(newLabel)
        #Return the dictionary
        return newLabel

def main():
    scmd = scMetadata()
    #Create a temporary file to append to.
    scmd.createLDPContainer("./", "testfolder")

if __name__ == "__main__":
    main()