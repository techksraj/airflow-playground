from airflow import DAG
from airflow.decorators import task
from airflow.operators.http import SimpleHttpOperator

from datetime import datetime

import json

with DAG('sharing_dag_api', start_date=datetime(2026, 1 ,1), schedule='@once', catchup=False) as dag:

    get_api_results_task = SimpleHttpOperator(
        task_id='get_api',
        endpoint="/entries",
        do_xcom_push=True,
        http_conn_id="api",
        method="GET"
    )

    @task 
    def parse_results(api_results):
        print(json.loads(api_results))

    parse_results(api_results=get_api_results_task.output)