# Metadata functions

from sarge import Command, Capture, get_stdout, get_stderr, capture_stdout
import provinator
import re
import ast

class scMetadata:
    def __init__(self):
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

