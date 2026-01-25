from airflow import DAG
from airflow.decorators import task

import random

from datetime import datetime, timedelta

with DAG(dag_id='dynamic_tasks_unknown_file_names', start_date=datetime(2026,1,1), schedule='@daily', catchup=False) as dag:

    @task
    def get_files():
        return ["file_{nb}" for nb in range(random.randint(3, 5))]

    @task
    def download_files(file: str):
        print(file)

    files = download_files.expand(file=get_files())