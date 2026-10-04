from fastapi.testclient import TestClient
from ghagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'list open pulls', **{'payload': {'pulls': [{'title': 'Add probes', 'state': 'open'}, {'title': 'WIP', 'state': 'closed'}]}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["open"] == ["Add probes"]
    refused = client.post("/agent/run", json={"goal": 'merge pull 12'}).json()
    assert refused["refused"] is True
