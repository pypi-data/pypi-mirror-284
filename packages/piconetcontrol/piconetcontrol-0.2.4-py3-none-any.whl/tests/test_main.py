

def test_client_ping(client):
    r = client.send_command(action="ping")
    assert r["action"] == "ping"
    assert r["time_responded"] > r["time_sent"]


def test_client_setup_write_read(client):
    cmds = [
        {"action": "setup_pin", "pin": 3, "mode": "output", "value": 0},
        {"action": "read_pin", "pin": 3},
        {"action": "write_pin", "pin": 3, "value": 1},
        {"action": "read_pin", "pin": 3},
    ]
    responses = client.send_commands(cmds)
    assert responses[1]["value"] == 0
    assert responses[3]["value"] == 1
