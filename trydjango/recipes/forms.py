

from django import forms


from .models import Recipe
class RecipeForm(forms.Modelform):

    class Meta:
        model = Recipe
        fields = ["name", "description", "directions"]