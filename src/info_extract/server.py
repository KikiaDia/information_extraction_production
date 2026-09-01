import time, uuid
from fastapi import FastAPI, HTTPException
from info_extract.config import get_settings
from info_extract.contracts import ExtractionRequest, ExtractionResponse, HealthResponse, IssueResponse
from info_extract.factory import build_service

settings=get_settings()
service=build_service(settings)
app=FastAPI(title="Energy Information Extraction", version="0.2.0")

@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok",environment=settings.environment,release_id=settings.release_id)

@app.post("/extract", response_model=ExtractionResponse)
async def extract(payload: ExtractionRequest):
    rid=str(uuid.uuid4()); started=time.perf_counter()
    try:
        result=await service.extract(payload.text)
    except TimeoutError as exc:
        raise HTTPException(504,"Extraction timed out") from exc
    except RuntimeError as exc:
        raise HTTPException(503,str(exc)) from exc
    return ExtractionResponse(
        extraction=result.extraction,
        issues=[IssueResponse(field=i.field,message=i.message,severity=i.severity) for i in result.issues],
        needs_human_review=result.needs_human_review,
        request_id=rid,
        latency_ms=(time.perf_counter()-started)*1000,
        release_id=settings.release_id,
    )
