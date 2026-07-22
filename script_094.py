from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
 
with DAG(dag_id="rag_knowledge_base_elt",
         schedule="@daily",                        # keep the KB fresh daily
         start_date=datetime(2026, 1, 1),
         catchup=False) as dag:
 
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    index_task = PythonOperator(task_id="transform_and_index",
                                python_callable=transform_and_index)
 
    extract_task >> index_task                     # dependency: extract, then index
