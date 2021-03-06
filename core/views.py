from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import HabitForm, RecordForm
from .models import Habit, Record
# Create your views here.


def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'core/habit_list.html', {'habits': habits})


def habits_details(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    records = Record.objects.filter(habit=habit, owner=request.user)
    return render(request, "core/habit_details.html", {'habit': habit, 'pk':pk, 'records': records})


def habits_edit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect('habits-details', habit.pk)
    else:
        form = HabitForm(instance=habit)
    return render(request, 'core/habit_edit.html', {'form': form})


def habits_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('habits-list')


def habits_new(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.author = request.user
            habit.save()
            return redirect('habits-list')
    else:
        form = HabitForm()
    return render(request, 'core/habit_edit.html', {'form': form})

def track_habit(request, pk):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.owner = request.user
            record.habit = Habit.objects.get(pk=pk)
            try: 
                record.save()
                return redirect('habits-details', pk=pk)
            except:
                form = RecordForm()
                return render(request, 'core/habit_edit.html', {'form': form})
            
    else:
        form = RecordForm()
    return render(request, 'core/habit_edit.html', {'form': form})
