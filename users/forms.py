from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False,label="次回から自動でログインする")

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"] 