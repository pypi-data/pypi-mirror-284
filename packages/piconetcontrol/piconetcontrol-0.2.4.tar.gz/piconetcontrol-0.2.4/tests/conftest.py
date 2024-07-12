

import pytest
from piconetcontrol.client import Client


@pytest.fixture(scope="session")
def client() -> Client:
    return Client()


@pytest.fixture
def action_ping(client):
    return client.send_command(action="ping")

