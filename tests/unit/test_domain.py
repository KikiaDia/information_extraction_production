from info_extract.domain import normalize, validate_business_rules
from info_extract.schema import EnergyDocumentExtraction

def test_normalize_equipment_id():
    x=normalize(EnergyDocumentExtraction(document_type="maintenance_report",equipment_id="tr-42",confidence=.9))
    assert x.equipment_id=="TR-42"

def test_incident_requires_safety_constraint():
    x=EnergyDocumentExtraction(document_type="incident_report",equipment_id="CB-7",confidence=.9)
    assert any(i.field=="safety_constraint" for i in validate_business_rules(x))
