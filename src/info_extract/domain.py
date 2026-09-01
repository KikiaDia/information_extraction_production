from dataclasses import dataclass
from info_extract.schema import EnergyDocumentExtraction


@dataclass(frozen=True)
class ValidationIssue:
    field: str
    message: str
    severity: str = "error"


def normalize(value: EnergyDocumentExtraction) -> EnergyDocumentExtraction:
    data=value.model_dump()
    for key, val in data.items():
        if isinstance(val, str):
            data[key]=" ".join(val.split()).strip() or None
    if data.get("equipment_id"):
        data["equipment_id"]=data["equipment_id"].upper()
    return EnergyDocumentExtraction(**data)


def validate_business_rules(value: EnergyDocumentExtraction) -> list[ValidationIssue]:
    issues=[]
    if value.document_type != "unknown" and not value.equipment_id:
        issues.append(ValidationIssue("equipment_id","required for identified operational documents"))
    if value.confidence is not None and value.confidence < 0.6:
        issues.append(ValidationIssue("confidence","requires human review","warning"))
    if value.document_type == "incident_report" and not value.safety_constraint:
        issues.append(ValidationIssue("safety_constraint","incident reports require safety review"))
    return issues
