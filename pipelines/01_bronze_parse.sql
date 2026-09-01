-- Databricks IDP skeleton: parse binary documents from governed storage.
-- Exact source table/volume and options are environment-specific.
CREATE OR REPLACE TABLE ${catalog}.${schema}.idp_bronze AS
SELECT
  path,
  ai_parse_document(content) AS parsed_document,
  current_timestamp() AS processed_at
FROM read_files('${source_path}', format => 'binaryFile');
