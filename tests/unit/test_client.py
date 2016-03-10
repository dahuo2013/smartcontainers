import pytest
import tarfile
import time

def test_Client(createClient):
    createClient.info()

def test_simple_tar(createClient):
    #Create the smartcontainer client
    #myClient = client.scClient()
    #Create a test file to be turned into a tar
    with open('tempprov.txt', 'a') as provfile:
        provfile.write('This is the data for the tar file test.')
    #Call the simple tar function and test the result
    thisfile = createClient.simple_tar('tempprov.txt')
    assert tarfile.is_tarfile(thisfile.name)

def test_hasProv(createClient, pull_docker_image):
    # myClient = client.scClient()
    newContainer = createClient.create_container(image='phusion/baseimage', command="/bin/bash", tty=True)
    ContainerID = str(newContainer['Id'])
    createClient.start(ContainerID)
    #assert createClient.hasProv(ContainerID, 'SCProv.jsonld', '/SmartContainer/')
    time.sleep(1)
    createClient.stop(ContainerID)
    createClient.remove_container(ContainerID)
