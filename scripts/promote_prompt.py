import argparse, mlflow
p=argparse.ArgumentParser()
p.add_argument("--name",required=True); p.add_argument("--from-alias",required=True); p.add_argument("--to-alias",required=True)
a=p.parse_args()
src=mlflow.genai.load_prompt(f"prompts:/{a.name}@{a.from_alias}")
try:
    cur=mlflow.genai.load_prompt(f"prompts:/{a.name}@{a.to_alias}")
    mlflow.genai.set_prompt_alias(name=a.name,alias=f"{a.to_alias}-previous",version=cur.version)
except Exception: pass
mlflow.genai.set_prompt_alias(name=a.name,alias=a.to_alias,version=src.version)
