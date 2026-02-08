from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

with DAG('map_dag', start_date=datetime(2026, 1 ,1), schedule='@once') as dag:

    start = PythonOperator(
        task_id='start',
        python_callable=lambda: ['/usr/folder_a', '/usr/folder_b', '/usr/folder_c']
    )

    new_list = start.output.map(lambda path: path + 'data/')

    end = PythonOperator(
        task_id='end',
        python_callable=lambda new_list: print([path for path in new_list]),
        op_args=[new_list]
    )