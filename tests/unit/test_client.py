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

def test_fileCopyIn(createClient, pull_docker_image):
    newContainer = createClient.create_container(image=pull_docker_image, 
                                                 command="/bin/sh", tty=True)
    ContainerID = str(newContainer['Id'])
    createClient.start(ContainerID)
    with open('SCProv.jsonld', 'a') as provfile:
        provfile.write('This is the data for the tar file test.')
    createClient.fileCopyIn(ContainerID,'SCProv.jsonld','/')
    assert createClient.hasProv(ContainerID, 'SCProv.jsonld', '/SmartContainer')
    time.sleep(1)
    createClient.stop(ContainerID)
    createClient.remove_container(ContainerID)
    os.remove('SCProv.jsonld')

def test_fileCopyOut(createClient, pull_docker_image):
    newContainer = createClient.create_container(image=pull_docker_image, command="/bin/sh", tty=True)
    ContainerID = str(newContainer['Id'])
    createClient.start(ContainerID)
    with open('SCProv.jsonld', 'a') as provfile:
        provfile.write('This is the data for the tar file test.')
    createClient.fileCopyIn(ContainerID,'SCProv.jsonld','/')
    createClient.fileCopyOut(ContainerID, 'SCProv.jsonld', '/SmartContainer/')
    assert os.path.isfile('SCProv.jsonld')
    time.sleep(1)
    createClient.stop(ContainerID)
    createClient.remove_container(ContainerID)
    os.remove('SCProv.jsonld')


def test_put_label_image(createClient, pull_docker_image):
    myLabel = {'smartcontainer':'{"author":"Scott B. Szakonyi"}'}
    createClient.put_label_image(image=pull_docker_image,
                                 repository="phusion/baseimage", tag="tester", label=myLabel)
    # The new image created should be image[0]'s id
    image_list = createClient.images()
    image_id = image_list[0]['Id']
    myInspect = createClient.inspect_image(image_id)
    assert 'Szakonyi' in str(myInspect)
    createClient.remove_image(image_id)

