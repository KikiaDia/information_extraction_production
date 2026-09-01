import asyncio
from info_extract.backends import FakeExtractor

def test_extract_maintenance():
    x=asyncio.run(FakeExtractor().extract_text("Maintenance report. Equipment ID: TR-42. Oil leak. Action: inspect seals."))
    assert x.document_type=="maintenance_report"
    assert x.equipment_id=="TR-42"
    assert x.anomaly=="oil leak"
