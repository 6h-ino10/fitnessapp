from django.core.management.base import BaseCommand
from exercise_app.api_utils import fetch_and_save_exercise_data
import requests

class Command(BaseCommand):
    help = 'Fetch exercises from API and save to database'

    def handle(self,*args,**kwargs):
        fetch_and_save_exercise_data()
        print("エクササイズデータを取得しました")