
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def sum_numbers(numbers):
   import json
   import ast

   # Normalize input to an iterable of numbers
   if isinstance(numbers, str):
       try:
           nums = json.loads(numbers)
       except Exception:
           nums = ast.literal_eval(numbers)
   else:
       nums = numbers or []

   total = 0
   for val in nums:
       total += val
   return total

with DAG(
   dag_id="templating_dag_python",
   start_date=datetime(2026, 1, 1),
   schedule=None,
   catchup=False) as dag:

       sum_nb = PythonOperator(
           task_id="sum_nb",
           python_callable=sum_numbers,
           op_kwargs={"numbers": "{{ dag_run.conf['numbers'] }}"},
       )