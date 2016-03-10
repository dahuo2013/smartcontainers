import pytest
import tarfile
import time
import os

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

def test_fileCopyIn(createClient,pull_docker_image):
    newContainer = createClient.create_container(image='phusion/baseimage:latest', 
                                                 command="/bin/bash", tty=True)
    ContainerID = str(newContainer['Id'])
    createClient.start(ContainerID)
    with open('SCProv.jsonld', 'a') as provfile:
        provfile.write('This is the data for the tar file test.')
    createClient.fileCopyIn(ContainerID,'SCProv.jsonld','/SmartContainer/')
    assert createClient.hasProv(ContainerID, 'SCProv.jsonld', '/SmartContainer/')
    time.sleep(1)
    createClient.stop(ContainerID)
    createClient.remove_container(ContainerID)
    os.remove('SCProv.jsonld')

#def test_fileCopyOut(createClient):
#    newContainer = createClient.create_container(image='phusion/append', command="/bin/bash", tty=True)
#    ContainerID = str(newContainer['Id'])
#    createClient.start(ContainerID)
#    createClient.fileCopyOut(ContainerID, 'SCProv.jsonld', '/SmartContainer/')
#    assert os.path.isfile('SCProv.jsonld')
#    time.sleep(1)
#    createClient.stop(ContainerID)
#    createClient.remove_container(ContainerID)
#    os.remove('SCProv.jsonld')

#def test_hasProv(createClient, pull_docker_image):
    # myClient = client.scClient()
#    newContainer = createClient.create_container(image='phusion/baseimage', command="/bin/bash", tty=True)
#    ContainerID = str(newContainer['Id'])
#    createClient.start(ContainerID)
#    assert createClient.hasProv(ContainerID, 'SCProv.jsonld', '/SmartContainer/')
#    time.sleep(1)
#    createClient.stop(ContainerID)
#    createClient.remove_container(ContainerID)

#def test_put_label_image(createClient):
#    myLabel = {'smartcontainer':'{"author":"Scott B. Szakonyi"}'}
#    createClient.put_label_image(imageID='f7874cea1543', label=myLabel, repository='Test', author=None, conf=None, tag=None, message=None)
#    myInspect = createClient.inspect_image('Test')
#    assert 'Szakonyi' in str(myInspect)
#    createClient.remove_image('Test')

