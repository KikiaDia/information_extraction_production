import json, os
from pathlib import Path
import mlflow
rows=json.loads(Path("evaluation/golden_dataset.json").read_text())
ds=mlflow.genai.datasets.get_dataset(os.environ["EVAL_DATASET_NAME"])
ds.merge_records([
  {"inputs":{"text":r["text"]},"expectations":r["expected"],
   "tags":{"case_id":r["id"],"schema_version":os.getenv("EXTRACTION_SCHEMA_VERSION","1.0.0"),"git_sha":os.getenv("CI_COMMIT_SHA","local")}}
  for r in rows
])
print(f"Synced {len(rows)} rows")
