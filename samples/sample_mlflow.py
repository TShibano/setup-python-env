#
# file: sample_mlflow.py
# auther: citrus
# date: 2025/05/01

# %% ---------------------------------
# ---- Abstract
# mlflowのテスト接続を行う
# ------------------------------------

# %% ---------------------------------
# ---- import libraries
# ------------------------------------
import polars as pl  # noqa
import mlflow


# 現在のトラッキングURIを表示
MLFLOW_URI = "http://xxxx"  # MLflow Tracking ServerのURLを記載
mlflow.set_tracking_uri(uri=MLFLOW_URI)  # MLflow Tracking ServerのURLを指定
tracking_uri = mlflow.get_tracking_uri()
print(f"Tracking URI: {tracking_uri}")

# %%
# 接続確認：experiment 一覧を取得（接続できないと例外が出る）
try:
    experiments = mlflow.search_experiments()
    print(f"Connected to MLflow Tracking Server at: {tracking_uri}")
    print("Available experiments:")
    for exp in experiments:
        print(f" - {exp.name} (ID: {exp.experiment_id})")
except Exception as e:
    print(f"Failed to connect to MLflow Tracking Server at {tracking_uri}")
    print(f"Error: {e}")

# %%
mlflow.set_experiment("sample_experiment")  # experimentの作成
# %%
with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("foo", 1)
    mlflow.log_artifact("../samples/sample_mlflow.py")

# %%
