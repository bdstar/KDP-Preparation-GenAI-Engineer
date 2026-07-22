# Experiment tracking with MLflow (illustrative): log config, metrics, artifacts.
import mlflow
 
with mlflow.start_run(run_name="qlora-domain-tune"):
    mlflow.log_params({"rank": 16, "alpha": 32, "lr": 2e-4, "epochs": 2})  # config
    # ... run training / evaluation ...
    mlflow.log_metrics({"eval_faithfulness": 0.88, "eval_loss": 0.41})     # results
    mlflow.log_artifact("./adapter")             # the trained adapter, versioned
# Runs are now comparable in the MLflow UI; the model registry versions the result.
