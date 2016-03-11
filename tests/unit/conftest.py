import os
import stat
import pytest

from sc import client
from docker import tls

@pytest.fixture(scope="session")
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

@pytest.fixture(scope="session")
def pull_docker_image(request, createClient):
    image_name = "alpine"
    createClient.pull(image_name+":latest")
    def fin():
        createClient.remove_image(image_name+":latest")
    request.addfinalizer(fin)
    return image_name
