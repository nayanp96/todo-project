from dataclasses import field
from django import forms
from .models import Mytodo

class Todoform(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ['task','date_time']
