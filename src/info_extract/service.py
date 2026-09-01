import asyncio
from dataclasses import dataclass
from info_extract.backends import Extractor
from info_extract.domain import normalize, validate_business_rules
from info_extract.schema import EnergyDocumentExtraction


@dataclass(frozen=True)
class ExtractionResult:
    extraction: EnergyDocumentExtraction
    issues: tuple
    needs_human_review: bool


class ExtractionService:
    def __init__(self, extractor: Extractor, timeout_seconds: float=30):
        self.extractor=extractor
        self.timeout_seconds=timeout_seconds

    async def extract(self, text: str) -> ExtractionResult:
        raw=await asyncio.wait_for(self.extractor.extract_text(text), timeout=self.timeout_seconds)
        normalized=normalize(raw)
        issues=tuple(validate_business_rules(normalized))
        needs_review=any(i.severity=="error" for i in issues) or any(
            i.field=="confidence" for i in issues
        )
        return ExtractionResult(normalized, issues, needs_review)
