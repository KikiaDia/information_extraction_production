-- Schema-driven extraction from parsed content.
CREATE OR REPLACE TABLE ${catalog}.${schema}.idp_silver AS
SELECT
  path,
  ai_extract(parsed_document, '${extraction_schema_json}') AS extraction,
  processed_at
FROM ${catalog}.${schema}.idp_bronze;
