"""Normalize extracted structs, apply deterministic business validation,
quarantine invalid/low-confidence rows for human review, and MERGE valid rows
idempotently into Gold Delta tables.
"""
