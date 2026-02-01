from airflow.decorators import dag, task

from datetime import datetime

@dag(start_date=datetime(2026,1,1), schedule="@once")
def decorator_dag():

    @task
    def start():
        return "start"
    
    @task.branch
    def choose_task(next_task: str):
        return next_task
    
    @task
    def success():
        print("success")

    @task
    def failure():
        print("failure")

    choose_task(start()) >> [success(), failure()]

decorator_dag()