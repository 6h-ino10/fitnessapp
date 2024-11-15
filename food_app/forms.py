from django import forms

class RecipeURLForm(forms.Form):
    url = forms.URLField(label='レシピURL',required=True)