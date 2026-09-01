import re
from typing import Protocol
from info_extract.schema import EnergyDocumentExtraction


class Extractor(Protocol):
    async def extract_text(self, text: str) -> EnergyDocumentExtraction: ...


class FakeExtractor:
    async def extract_text(self, text: str) -> EnergyDocumentExtraction:
        low=text.lower()
        equipment_match=re.search(r"(?:equipment|asset)\s*(?:id)?\s*[:#-]?\s*([A-Za-z0-9-]+)", text, re.I)
        site_match=re.search(r"site\s*[:#-]?\s*([A-Za-z0-9 _-]+)", text, re.I)
        document_type = (
            "incident_report" if "incident" in low else
            "maintenance_report" if "maintenance" in low else
            "inspection_report" if "inspection" in low else "unknown"
        )
        return EnergyDocumentExtraction(
            document_type=document_type,
            equipment_id=equipment_match.group(1) if equipment_match else None,
            site=site_match.group(1).strip() if site_match else None,
            anomaly="oil leak" if "oil leak" in low else None,
            action_required="inspect seals" if "inspect seals" in low else None,
            safety_constraint="isolate equipment" if "isolate equipment" in low else None,
            confidence=0.95 if document_type != "unknown" else 0.5,
        )


class DatabricksIDPExtractor:
    """Adapter for Databricks IDP SQL functions.

    Production batch processing should normally use Spark/Lakeflow directly over
    governed binary/text columns rather than call this adapter one document at a time.
    """

    def __init__(self, warehouse_id: str, extraction_schema_json: str):
        self.warehouse_id=warehouse_id
        self.extraction_schema_json=extraction_schema_json

    async def extract_text(self, text: str) -> EnergyDocumentExtraction:
        try:
            from databricks import sql
            from databricks.sdk.core import Config
        except ImportError as exc:
            raise RuntimeError('Install Databricks extras: pip install -e ".[databricks]"') from exc

        cfg=Config()
        with sql.connect(
            server_hostname=cfg.host.replace("https://",""),
            http_path=f"/sql/1.0/warehouses/{self.warehouse_id}",
            credentials_provider=lambda: cfg.authenticate,
        ) as conn:
            with conn.cursor() as cur:
                # Parameterized source text; schema is controlled application configuration.
                cur.execute(
                    "SELECT ai_extract(?, ?) AS extraction",
                    [text, self.extraction_schema_json],
                )
                row=cur.fetchone()
        raw=row[0]
        if isinstance(raw, str):
            import json
            raw=json.loads(raw)
        return EnergyDocumentExtraction.model_validate(raw)
