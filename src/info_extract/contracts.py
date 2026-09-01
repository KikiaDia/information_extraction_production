from pydantic import BaseModel, Field
from info_extract.schema import EnergyDocumentExtraction


class ExtractionRequest(BaseModel):
    text: str=Field(min_length=1,max_length=100000)
    source_id: str | None=None


class IssueResponse(BaseModel):
    field: str
    message: str
    severity: str


class ExtractionResponse(BaseModel):
    extraction: EnergyDocumentExtraction
    issues: list[IssueResponse]
    needs_human_review: bool
    request_id: str
    latency_ms: float
    release_id: str


class HealthResponse(BaseModel):
    status: str
    environment: str
    release_id: str
