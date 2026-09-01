"""Controlled reprocessing entry point.

Reprocessing must identify source snapshot, extraction schema version, code release,
target table and write mode. Prefer idempotent MERGE semantics and keep old Delta
versions available for audit/rollback.
"""
