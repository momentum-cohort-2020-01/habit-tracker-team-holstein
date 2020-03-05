from django import forms
from .models import Habit
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ("name", "goal", "unit",)