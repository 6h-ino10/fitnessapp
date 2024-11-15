from django.shortcuts import render
import requests
from .forms import RecipeURLForm

# Create your views here.

def get_recipe_nutrition(request):
    nutrition_data = None
    error_message = None

    if request.method == 'POST':
        form = RecipeURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            api_url = "https://api.edamam.com/api/nutrition-details"
            app_id = "1c64a44d"
            app_key = "38fca3de28d255dd7c80042956083b25"

            headers = {"Content-Type":"application/json"}
            payload = {
                "title":"Recipe from external site",
                "ingr":["1 serving"],
                "url":url
                }

            response = requests.post(api_url,headers=headers,json=payload)

            if response.status_code == 200:
                nutrition_data = response.json()
            else:
                error_message = "エラーが発生しました:ステータスコード{response.status_code}"
        else:
            form = RecipeURLForm()

        return render(request,'get_recipe_nutrition.html',{
            'form':form,
            'nutrition_data':nutrition_data,
            'error_message':error_message 
        })
