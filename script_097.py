import mlflow
 
def record_tuning_run(config: dict, eval_results: dict):
    with mlflow.start_run():
        mlflow.log_params(config)          # e.g. model, prompt version, top_k
        mlflow.log_metrics(eval_results)   # e.g. faithfulness, latency, cost
    # Compare runs in the MLflow UI to choose the best configuration deliberately.
