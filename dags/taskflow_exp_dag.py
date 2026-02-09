from airflow.decorators import dag, task

from datetime import datetime

@dag(start_date=datetime(2024, 6, 1), schedule='@once', catchup=False)
def taskflow_exp_dag():

    @task
    def start():
        return 'success'
    
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

taskflow_exp_dag()