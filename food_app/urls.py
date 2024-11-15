from django.urls import path
from . import views

urlpatterns = [
    path('get_recipe_nutrition/',views.get_recipe_nutrition,name='get_recipe_nutrition'),
]
