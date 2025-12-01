from django import forms
from django.forms import ModelForm

from staffapp.models import Expenses


class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expenses
        fields='__all__'
        widgets={
            'description':forms.TextInput(attrs={'placeholder':'Enter expense description'}),
            'amount':forms.NumberInput(attrs={'placeholder':'Enter expense amount'}),
            'date':forms.DateInput(attrs={'placeholder':'Enter the date'}),
        }
