from airflow import DAG
from airflow.decorators import task

from datetime import datetime, timedelta

with DAG(dag_id='dynamic_tasks', start_date=datetime(2026,1,1), schedule='@daily', catchup=False) as dag:

    @task
    def download_files(file: str):
        print(file)

    files = download_files.expand(file=["file_a","file_b","file_c"])