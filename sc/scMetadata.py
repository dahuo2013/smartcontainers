# Metadata functions
# Metadata should 

from sarge import Command, Capture, get_stdout, get_stderr, capture_stdout
import provinator
import re
import ast

class scMetadata:
    def __init__(self, provfilename, provfilepath):
        #initial scMetadata
        self.provenance = Dataset(default_union=True)
        ds = Dataset(default_union=True)

		# JSON-LD serializer requires an explicit context.
		# https://github.com/RDFLib/rdflib-jsonld
		# context = {"@vocab": "http://purl.org/dc/terms/", "@language": "en"}

		context = {"prov": "http://www.w3.org/ns/prov#",
           "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
           "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
           "xsd": "http://www.w3.org/2001/XMLSchema#",
           "dc": "http://purl.org/dc/terms"}

		# Define some namespaces
		PROV = Namespace("http://www.w3.org/ns/prov#")
		ORE = Namespace("http://www.openarchives.org/ore/terms/")
		OWL = Namespace("http://www.w3.org/2002/07/owl#")
		DC = Namespace("http://purl.org/dc/terms/")
		UUIDNS = Namespace("urn:uuid:")
		DOCKER = Namespace("http://w3id.org/daspos/docker#")
		# W3C namespace:
		POSIX = Namespace("http://www.w3.org/ns/posix/stat#")
		ACL = Namespace("http://www.w3.org/ns/auth/acl#")

		# DASPOS namespaces
		SC = Namespace("https://w3id.org/daspos/smartcontainers#")
		CA = Namespace("https://w3id.org/daspos/computationalactivity#")
		CE = Namespace("https://w3id.org/daspos/computationalenvironment#")


		# Need to handle DOI
		# http://bitwacker.com/2010/02/04/dois-uris-and-cool-resolution/

		ds.bind("prov", PROV)
		ds.bind("ore", ORE)
		ds.bind("owl", OWL)
		ds.bind("dc", DC)
		ds.bind("uuidns", UUIDNS)
		ds.bind("docker", DOCKER)
		ds.bind("posix", POSIX)
		ds.bind("acl", ACL)
		ds.bind("sc", SC)
		ds.bind("ca", CA)
		ds.bind("ce", CE)

		default_graph = ds
        self.provfilepath = provfilepath
        self.provfilename = provfilename
        self.label_prefix = "smartcontainer"

    def createLDPContainer(self, url):
    	#create LDP Container
    	#docker create file folder
    	#docker create file
    	#append LDP Container meta
    	pass

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

