import json
from pathlib import Path
from info_extract.backends import FakeExtractor, DatabricksIDPExtractor
from info_extract.config import Settings
from info_extract.service import ExtractionService


def build_service(settings: Settings) -> ExtractionService:
    if settings.backend=="databricks":
        schema=Path(__file__).with_name("extraction_schema.json").read_text()
        extractor=DatabricksIDPExtractor(settings.sql_warehouse_id, schema)
    else:
        extractor=FakeExtractor()
    return ExtractionService(extractor)
