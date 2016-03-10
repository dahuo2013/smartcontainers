import pytest

@pytest.fixture(scope="module")
def pull_docker_image(request):
    image_name = "phusion/baseimage:latest"
    from sc import dockercli
    dockercli.DockerCli("").dcli.pull(image_name)
    def fin():
        dockercli.DockerCli("").dcli.remove_image(image_name)
    request.addfinalizer(fin)
