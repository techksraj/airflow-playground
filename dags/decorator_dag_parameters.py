from airflow.decorators import dag, task

from datetime import datetime

@dag(start_date=datetime(2026,1,1), schedule="@once")
def decorator_dag_parameters():

    @task(retries=3)
    def start():
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

decorator_dag_parameters()