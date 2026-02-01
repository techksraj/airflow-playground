from airflow.decorators import dag, task
from airflow.operators.python import get_current_context

from datetime import datetime

@dag(start_date=datetime(2026,1,1), schedule="@once")
def decorator_dag_access_context_vars():

    # Method 1: 
    # @task(retries=3)
    # def start(ti=None, ds=None):
    #     print(f"Task instance: {ti}")
    #     print(f"Dataset: {ds}")
    #     return "start"
    
    # Method 2: Using **context to access all context variables
    # @task(retries=3)
    # def start(**context):
    #     print(f"Context: {context}")
    #     return "start"
    
    #Method 3: Using get_current_context()
    @task(retries=3)
    def start():
        context = get_current_context()
        print(f"Context: {context}")
        return "start"

    
    @task.branch
    def choose_task(next_task: str):
        return next_task
    
    @task(retries=1)
    def success():
        print("success")

    @task
    def failure():
        print("failure")

    choose_task(start()) >> [success(), failure()]

decorator_dag_access_context_vars()