from datetime import date
from datetime import timedelta
import datetime
import requests

from airflow.decorators import dag, task
from airflow.operators.python import get_current_context

default_args = {
'owner': 'soreshnikov',
'depends_on_past': False,
'retries': 2,
'retry_delay': timedelta(minutes=5),
'start_date': datetime(2022, 12, 1),
}
      
# Интервал запуска DAG

schedule_interval = '1 11 * * *'

@dag(default_args=default_args, schedule_interval=schedule_interval, catchup=False)
def soreshnikov_feed_report():    

    @task
    def extract_metrics():
        q = "hey from dag"
    
    @task
    def send_message():
        message="hey from dagger"
        
soreshnikov_feed_report=soreshnikov_feed_report()