from django.contrib import admin
from django.urls import path
from users import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('signup_complete/',views.SignupCompleteView.as_view(),name='signup_complete'),
    path('home/',views.HomeView.as_view(),name='home'),
    path('get_recipe_nutrition/',views.get_recipe_nutrition,name='get_recipe_nutrition'),
]
