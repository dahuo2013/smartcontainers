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
        myclient = client.scClient(base_url=docker_host_https, tls=tls_config,
                                   version="auto")
        return myclient
# If we fall through, myclient is set to none and we should fail.
    return myclient


def test_Client(createClient):
    createClient.info()

#def test_simple_tar():
#    #Create the smartcontainer client
#    myClient = client.scClient()
#    #Create a test file to be turned into a tar
#    with open('tempprov.txt', 'a') as provfile:
#        provfile.write('This is the data for the tar file test.')
#    #Call the simple tar function and test the result
#    thisfile = myClient.simple_tar('tempprov.txt')
#    assert tarfile.is_tarfile(thisfile.name)

#def test_hasProv():
#    myClient = client.scClient()
#    newContainer = myClient.dcli.create_container(image='phusion/append', command="/bin/bash", tty=True)
#    ContainerID = str(newContainer['Id'])
#    myClient.dcli.start(ContainerID)
#    assert myClient.hasProv(ContainerID, 'SCProv.jsonld', '/SmartContainer/')
#    time.sleep(1)
#    myClient.dcli.stop(ContainerID)
#    myClient.dcli.remove_container(ContainerID)
