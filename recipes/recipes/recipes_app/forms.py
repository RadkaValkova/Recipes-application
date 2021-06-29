from django import forms

from recipes.recipes_app.models import RecipeModel


# class BootstrapFormMixin:
#     def _init_bootstrap(self):
#         for (_, field) in self.fields.items():
#             field.widget.attrs = {
#                 'class': 'form-control',
#             }
#

class RecipeForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._init_bootstrap()

    class Meta:
        model = RecipeModel
        fields = '__all__'

