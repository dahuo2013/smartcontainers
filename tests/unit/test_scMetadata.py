import pytest
import os
import docker
from sc import scMetadata

def test_appendData():
    #Create scMetadata instance
    scmd = scMetadata.scMetadata()
    #Create a temporary file to append to.
    open('tempprov.txt', 'a').close()
    scmd.appendData('tempprov.txt')
    #Test that the file is not empty
    assert os.stat('tempprov.txt').st_size > 0
    os.remove('tempprov.txt')

def test_labelDictionary():
    #Create scMetadata instance
    scmd = scMetadata.scMetadata()
    #Call for the dictionary object
    thisObject = scmd.labelDictionary('smartcontainer')
    assert type(thisObject) == dict