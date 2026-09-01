import os,pytest
from info_extract.config import Settings

@pytest.mark.integration
def test_workspace_coordinates():
    if os.getenv("RUN_DATABRICKS_INTEGRATION")!="1":
        pytest.skip("Set RUN_DATABRICKS_INTEGRATION=1")
    s=Settings(backend="databricks")
    assert s.source_volume.startswith("/Volumes/")
    assert "." in s.bronze_table
    assert s.sql_warehouse_id
