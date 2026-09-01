from pydantic import BaseModel, Field
from typing import Literal


class EnergyDocumentExtraction(BaseModel):
    document_type: Literal[
        "maintenance_report","equipment_sheet","inspection_report",
        "incident_report","work_order","unknown"
    ] = "unknown"
    equipment_id: str | None = None
    site: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    intervention_date: str | None = None
    anomaly: str | None = None
    action_required: str | None = None
    safety_constraint: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
