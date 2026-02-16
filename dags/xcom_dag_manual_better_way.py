from airflow.sdk import dag, task, Context

@dag
def xcom_dag_manual_better_way():

    @task
    def task_a():
        val = 42
        return val

    @task
    def task_b(val: int):
        print(val)

    val = task_a()
    task_b(val)

xcom_dag_manual_better_way()