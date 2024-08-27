from django import forms
from .models import Food

class FoodCreateForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = (
            'title',
            'category',
            'description',
            'img',
            'price'
        )
class FoodUpdateForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = (
            'title',
            'category',
            'description',
            'img',
            'price'
        )