import asyncio, json, time
from pathlib import Path
from info_extract.backends import FakeExtractor
from info_extract.service import ExtractionService
from evaluation.scorers import field_metrics


async def main():
    cases=json.loads(Path("evaluation/golden_dataset.json").read_text())
    service=ExtractionService(FakeExtractor())
    all_metrics=[]; validations=[]; latencies=[]
    for case in cases:
        started=time.perf_counter()
        result=await service.extract(case["text"])
        latencies.append((time.perf_counter()-started)*1000)
        all_metrics.append(field_metrics(case["expected"], result.extraction.model_dump()))
        validations.append(not any(i.severity=="error" for i in result.issues))
    metrics={
      "field_f1":sum(m["f1"] for m in all_metrics)/len(all_metrics),
      "required_field_recall":sum(m["recall"] for m in all_metrics)/len(all_metrics),
      "validation_pass_rate":sum(validations)/len(validations),
      "p95_latency_ms":max(latencies),
    }
    Path("evaluation/results").mkdir(parents=True,exist_ok=True)
    Path("evaluation/results/offline_eval.json").write_text(json.dumps(metrics,indent=2))
    print(json.dumps(metrics,indent=2))
    return 1 if metrics["field_f1"] < 0.90 or metrics["required_field_recall"] < 0.95 else 0

if __name__=="__main__":
    raise SystemExit(asyncio.run(main()))
