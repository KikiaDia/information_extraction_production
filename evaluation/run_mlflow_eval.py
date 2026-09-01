"""Load governed MLflow Evaluation Dataset and evaluate the Databricks extraction path.

Recommended production scorers include per-field correctness, required-field recall,
schema validity, citation/evidence correctness when citations are enabled, human-review
rate, latency and cost.
"""
import os, mlflow
def main():
    mlflow.set_experiment(os.environ["MLFLOW_EXPERIMENT_NAME"])
    ds=mlflow.genai.datasets.get_dataset(os.environ["EVAL_DATASET_NAME"])
    print(ds)
if __name__=="__main__": main()
