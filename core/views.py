from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Habit
# Create your views here.


def habit_list(request):
    habit = Habit.objects.all()
    return render(request, 'core/habit_list.html', {})