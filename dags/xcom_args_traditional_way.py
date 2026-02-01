from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG('xcom_args_traditional_way', start_date=datetime(2022, 1 ,1), schedule='@once') as dag:

    start = PythonOperator(
        task_id='start',
        python_callable=lambda: 42
    )

    #other way of pulling xcom values using ti.xcom_pull
    #bash_command='echo {{ ti.xcom_pull(task_ids="start") }}'

    print = BashOperator(
        task_id='print',
        bash_command=f'echo "value from previosus task is {start.output}"'
    )