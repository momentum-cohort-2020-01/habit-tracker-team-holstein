from django import forms
from .models import Habit, Record
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ("name", "goal", "unit",)

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ("date", "achievement",)
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'}),
    }