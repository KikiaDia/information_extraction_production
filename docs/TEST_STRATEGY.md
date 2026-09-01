# Test strategy

- Unit: normalization, schema validation, business rules.
- Functional: API contract using deterministic fake extractor.
- Integration: ai_parse_document / ai_extract / SQL warehouse / UC permissions.
- Evaluation: per-field precision/recall/F1, required-field recall, schema validity,
  evidence/citation correctness if enabled, human-review rate.
- Data pipeline: idempotence, duplicate prevention, quarantine, reprocessing.
- Production: missingness drift, document-type mix drift, latency, throughput, failures,
  cost/document and human review.
