import mlflow
from contextlib import contextmanager


class ExperimentTracker:

    def __init__(self):

        mlflow.set_tracking_uri("file:./mlruns")

        mlflow.set_experiment("Enterprise-RAG")

    @contextmanager
    def run(self, run_name: str):

        with mlflow.start_run(run_name=run_name):

            yield

    @staticmethod
    def log_params(params: dict):

        mlflow.log_params(params)

    @staticmethod
    def log_metrics(metrics: dict):

        mlflow.log_metrics(metrics)

    @staticmethod
    def log_tags(tags: dict):

        mlflow.set_tags(tags)
