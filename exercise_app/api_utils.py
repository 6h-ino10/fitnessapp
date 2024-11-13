import requests
from .models import Exercise

def fetch_and_save_exercise_data():
    url = "https://exercisedb-api.vercel.app/api/v1/exercises"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exercises = data if isinstance(data,list) else data.get('data',{}).get('exercises',[])

        if exercises:
            for exercise in exercises:
                name = exercise.get('name','N/A')
                target_muscles = exercise.get('target','N/A')
                gif_url = exercise.get('gifUrl','N/A')
                exercise_id = exercise.get('id','N/A')
                calories_burned = exercise.get('calories_burned',0)

                Exercise.objects.get_or_create(
                    exercise_id=exercise_id,
                    defaults={
                        'name':name,
                        'target_muscles':target_muscles,
                        'gif_url':gif_url,
                        'calories_burned':calories_burned,
                    }
                )
            print("エクササイズデータが保存されました。")
        else:
            print("エクササイズデータが空です。")

    else:
        print("エラーが発生しました。ステータスコード:",response.status_code)

