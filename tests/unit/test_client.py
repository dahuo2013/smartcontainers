import pytest
import os
from sc import client
import tarfile
import time

def test_simple_tar():
    #Create the smartcontainer client
    myClient = client.scClient()
    #Create a test file to be turned into a tar
    with open('tempprov.txt', 'a') as provfile:
        provfile.write('This is the data for the tar file test.')
    #Call the simple tar function and test the result
    thisfile = myClient.simple_tar('tempprov.txt')
    assert tarfile.is_tarfile(thisfile.name)

def test_hasProv():
    myClient = client.scClient()
    newContainer = myClient.dcli.create_container(image='phusion/append') #, command="/bin/echo")
    ContainerID = newContainer['Id']
    myClient.dcli.start(ContainerID)
    #assert myClient.hasProv(ContainerID, 'SCProv.jsonld','/SmartContainer/')
    time.sleep(1)
    myClient.dcli.stop(ContainerID)
    myClient.dcli.remove_container(ContainerID)