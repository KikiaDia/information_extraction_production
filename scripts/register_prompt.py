import os, mlflow
template=open("prompts/extraction_guidance.txt",encoding="utf-8").read()
p=mlflow.genai.register_prompt(
 name=os.environ["PROMPT_NAME"], template=template,
 commit_message=os.getenv("PROMPT_COMMIT_MESSAGE","Extraction guidance from CI"),
 tags={"schema_version":os.getenv("EXTRACTION_SCHEMA_VERSION","1.0.0"),"git_sha":os.getenv("CI_COMMIT_SHA","local")}
)
print(f"{p.name} version={p.version}")
