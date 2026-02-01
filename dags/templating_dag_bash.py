from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG('templating_dag_bash', schedule='@daily', start_date=datetime(2026,1,1), 
         catchup=False, template_searchpath=['include']) as dag:

    run_this = BashOperator(
        task_id='run_this',
        bash_command="scripts/script.sh"
    )