from fastapi.testclient import TestClient
from info_extract.server import app
client=TestClient(app)

def test_health():
    assert client.get("/health").status_code==200

def test_extract_contract():
    r=client.post("/extract",json={"text":"Maintenance report. Equipment ID: TR-42. Oil leak. Action: inspect seals."})
    assert r.status_code==200
    body=r.json()
    assert body["extraction"]["equipment_id"]=="TR-42"
    assert "needs_human_review" in body
