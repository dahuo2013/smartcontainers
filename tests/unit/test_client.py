import pytest
import os
import stat
from sc import client
from docker import tls
import tarfile
import time

@pytest.fixture
def createClient():
    myclient = None
    # Find docker-machine environment variables
    docker_host = os.getenv("DOCKER_HOST")
    docker_cert_path = os.getenv("DOCKER_CERT_PATH")
    docker_machine_name = os.getenv("DOCKER_MACHINE_NAME")

    # Look for linux docker socket file
    path = "/var/run/docker.sock"
    isSocket = False
    if os.path.exists(path):
        mode = os.stat(path).st_mode
        isSocket = stat.S_ISSOCK(mode)
    if isSocket:
        docker_socket_file ="unix://"+path
        myclient = client.scClient(base_url=docker_socket_file, version="auto")
        return myclient
    elif (docker_host and docker_cert_path and docker_machine_name):
        tls_config = tls.TLSConfig(
            client_cert=(os.path.join(docker_cert_path, 'cert.pem'),
                         os.path.join(docker_cert_path,'key.pem')),
            ca_cert=os.path.join(docker_cert_path, 'ca.pem'),
            verify=True,
            assert_hostname = False
        )
        docker_host_https = docker_host.replace("tcp","https")
        myclient = client.scClient(base_url=docker_host_https, tls=tls_config, version="auto")
        return myclient
# If we fall through, myclient is set to none and we should fail.
    return myclient

def test_Client(createClient):
    createClient.info()

def test_simple_tar(createClient):
    #Create a test file to be turned into a tar
    with open('tempprov.txt', 'a') as provfile:
        provfile.write('This is the data for the tar file test.')
    #Call the simple tar function and test the result
    thisfile = createClient.simple_tar('tempprov.txt')
    assert tarfile.is_tarfile(thisfile.name)

def test_hasProv(createClient):
    # myClient = client.scClient()
    newContainer = createClient.create_container(image='phusion/append', command="/bin/bash", tty=True)
    ContainerID = str(newContainer['Id'])
    createClient.start(ContainerID)
    assert createClient.hasProv(ContainerID, 'SCProv.jsonld', '/SmartContainer/')
    time.sleep(1)
    createClient.stop(ContainerID)
    createClient.remove_container(ContainerID)

def test_fileCopyIn(createClient):
    newContainer = createClient.create_container(image='phusion/append', command="/bin/bash", tty=True)
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

def test_fileCopyOut(createClient):
    newContainer = createClient.create_container(image='phusion/append', command="/bin/bash", tty=True)
    ContainerID = str(newContainer['Id'])
    createClient.start(ContainerID)
    createClient.fileCopyOut(ContainerID, 'SCProv.jsonld', '/SmartContainer/')
    assert os.path.isfile('SCProv.jsonld')
    time.sleep(1)
    createClient.stop(ContainerID)
    createClient.remove_container(ContainerID)
    os.remove('SCProv.jsonld')

def test_put_label_image(createClient):
    myLabel = {'smartcontainer':'{"author":"Scott B. Szakonyi"}'}
    createClient.put_label_image(imageID='f7874cea1543', label=myLabel, repository='Test', author=None, conf=None, tag=None, message=None)
    myInspect = createClient.inspect_image('Test')
    assert 'Szakonyi' in str(myInspect)
    createClient.remove_image('Test')