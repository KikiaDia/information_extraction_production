# Reproducibility for Information Extraction

A reproducible IDP release identifies:
- code/artifact and dependency lock,
- extraction schema name/version/hash,
- parsing/extraction function configuration,
- optional guidance prompt name + immutable version,
- source corpus snapshot / UC Volume path,
- Bronze/Silver/Gold table coordinates and Delta versions,
- normalization + business validation code,
- evaluation dataset version + evaluation run,
- environment/DAB target and infrastructure config.

Why schema versioning matters: changing one field name/type/description can change output
semantics even when application code is unchanged.

Reprocessing must be explicit: choose an immutable release + source snapshot + schema
version and write idempotently. Rollback may restore a previous Gold Delta version or
reprocess with the previous complete release coordinates.
