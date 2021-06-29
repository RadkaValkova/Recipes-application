from django import forms

from recipes.recipes_app.models import RecipeModel


class RecipeForm(forms.ModelForm):


    class Meta:
        model = RecipeModel
        fields = '__all__'

