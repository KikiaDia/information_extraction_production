import os,httpx
base=os.environ["IE_BASE_URL"].rstrip("/")
assert httpx.get(base+"/health",timeout=10).status_code==200
r=httpx.post(base+"/extract",json={"text":"Maintenance report. Equipment ID: TR-42. Site: Lyon. Oil leak detected. Action: inspect seals."},timeout=30)
r.raise_for_status()
assert r.json()["extraction"]["equipment_id"]=="TR-42"
print("smoke OK")
