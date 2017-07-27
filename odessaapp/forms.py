from django import forms
from odessaapp.models import DailyDish

class DailyDishForm(forms.ModelForm):
    class Meta:
        model = DailyDish
        fields = ['name', 'description']

