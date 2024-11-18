from django.shortcuts import render
import requests
from .forms import RecipeURLForm

# Create your views here.

def get_recipe_nutrition(request):
    print("ビューが呼び出されました。")
    nutrition_data = None
    error_message = None
    app_id = "1c64a44d"
    app_key = "75e2b1614ddeef2d1e9aedbb3a1d25e3"


    form = RecipeURLForm()

    if request.method == 'POST':
        print("POSTリクエストを受け取りました。")
        form = RecipeURLForm(request.POST)
        if form.is_valid():
            print("フォームが有効です。")
            url = form.cleaned_data['url']
            api_url = f"https://api.edamam.com/api/nutrition-details?app_id={app_id}&app_key={app_key}"

            headers = {"Content-Type":"application/json"}
            payload = {
                "title":"Recipe from external site",
                "ingr":["1 serving"],
                "url":url
                }
            
            try:
                response = requests.post(api_url,headers=headers,json=payload)
                print(f"APIステータスコード:{response.status_code}")

                if response.status_code == 200:
                    nutrition_data = response.json()
                else:
                    error_message = f"エラーが発生しました:ステータスコード{response.status_code}"
            except Exception as e:
                error_message = f"APIリクエスト中に例外が発生しました:{e}"
                print(error_message)

        else:
            form = RecipeURLForm()

        
    print("テンプレートをレンダリングします")
    return render(request,'get_recipe_nutrition.html',{
        'form':form,
        'nutrition_data':nutrition_data,
        'error_message':error_message 
        })
