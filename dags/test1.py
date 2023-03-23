import telegram
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
'start_date': datetime(2022, 3, 10),
}

my_token='5655432903:AAFf2y8CEVLfWFBcaryZJ9VPF6H2LWSyDgg'
bot = telegram.Bot(token=my_token)
chat_id=261609763
      
# Интервал запуска DAG

schedule_interval = '1 11 * * *'

@dag(default_args=default_args, schedule_interval=schedule_interval, catchup=False)
def soreshnikov_feed_report():    

    @task
    def extract_metrics():
        q = 2+2
    
    @task
    def send_message():
        message=q
        bot.sendMessage(chat_id=chat_id,text=message)
    

        
soreshnikov_feed_report=soreshnikov_feed_report()