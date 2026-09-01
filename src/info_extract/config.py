from functools import lru_cache
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env", extra="ignore")

    environment: Literal["local","dev","staging","prod"]="local"
    backend: Literal["fake","databricks"]="fake"

    extraction_schema_name: str="energy_maintenance_v1"
    extraction_schema_version: str="1.0.0"
    extraction_model_type: str="ai_extract"
    parse_model_type: str="ai_parse_document"
    prompt_name: str="main.genai.energy_extraction_guidance"
    prompt_ref: str="dev"

    bronze_table: str="main.genai.idp_bronze"
    silver_table: str="main.genai.idp_silver"
    gold_table: str="main.genai.idp_gold"
    source_volume: str="/Volumes/main/genai/energy_documents"
    sql_warehouse_id: str=""

    eval_dataset_name: str="main.genai.info_extraction_eval"
    mlflow_experiment_name: str="/Shared/information-extraction"

    min_field_f1: float=0.90
    min_required_field_recall: float=0.95
    min_validation_pass_rate: float=0.98
    max_p95_latency_ms: float=12000.0
    release_id: str="local"


@lru_cache
def get_settings(): return Settings()
