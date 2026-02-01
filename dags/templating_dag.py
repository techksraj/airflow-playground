from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


from datetime import datetime

with DAG('templating_dag', schedule='@daily', start_date=datetime(2026, 1, 1), catchup=False) as dag:

    get_data = SQLExecuteQueryOperator(
        task_id='get_data',
        conn_id='postgres',
        sql="SELECT EXISTS (SELECT 1 FROM my_table WHERE date='{{ ds }}')",
    )