import hashlib,json,os,platform
from pathlib import Path
def sha(p):
    x=Path(p); return hashlib.sha256(x.read_bytes()).hexdigest() if x.exists() else None
manifest={
 "release":{"id":os.getenv("RELEASE_ID"),"git_sha":os.getenv("CI_COMMIT_SHA"),"artifact_digest":os.getenv("ARTIFACT_DIGEST")},
 "runtime":{"python":platform.python_version(),"lock_sha256":sha("requirements.lock")},
 "environment":{"name":os.getenv("ENVIRONMENT"),"bundle_target":os.getenv("BUNDLE_TARGET")},
 "idp":{"parse_function":os.getenv("PARSE_MODEL_TYPE","ai_parse_document"),"extract_function":os.getenv("EXTRACTION_MODEL_TYPE","ai_extract"),"schema_name":os.getenv("EXTRACTION_SCHEMA_NAME"),"schema_version":os.getenv("EXTRACTION_SCHEMA_VERSION"),"schema_sha256":sha("src/info_extract/extraction_schema.json"),"prompt_name":os.getenv("PROMPT_NAME"),"prompt_version":os.getenv("PROMPT_RESOLVED_VERSION")},
 "data":{"source_volume":os.getenv("SOURCE_VOLUME"),"source_snapshot":os.getenv("SOURCE_SNAPSHOT"),"bronze_table":os.getenv("BRONZE_TABLE"),"silver_table":os.getenv("SILVER_TABLE"),"gold_table":os.getenv("GOLD_TABLE"),"gold_delta_version":os.getenv("GOLD_DELTA_VERSION")},
 "evaluation":{"dataset":os.getenv("EVAL_DATASET_NAME"),"dataset_version":os.getenv("EVAL_DATASET_VERSION"),"run_id":os.getenv("EVALUATION_RUN_ID"),"golden_sha256":sha("evaluation/golden_dataset.json"),"report_sha256":sha("evaluation/results/offline_eval.json")},
 "deployment":{"databricks_yml_sha256":sha("databricks.yml")}
}
Path("release-manifest.json").write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
