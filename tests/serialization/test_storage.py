import prefect
from prefect.environments import storage
from prefect.serialization.storage import BaseStorageSchema, DockerSchema, MemorySchema


def test_docker_empty_serialize():
    docker = storage.Docker()
    serialized = DockerSchema().dump(docker)

    assert serialized
    assert serialized["__version__"] == prefect.__version__
    assert not serialized["image_name"]
    assert not serialized["image_tag"]
    assert not serialized["registry_url"]


def test_memory_serialize():
    s = storage.Memory()
    serialized = MemorySchema().dump(s)

    assert serialized == {"__version__": prefect.__version__}


def test_docker_full_serialize():
    docker = storage.Docker(registry_url="url", image_name="name", image_tag="tag")
    serialized = DockerSchema().dump(docker)

    assert serialized
    assert serialized["__version__"] == prefect.__version__
    assert serialized["image_name"] == "name"
    assert serialized["image_tag"] == "tag"
    assert serialized["registry_url"] == "url"
