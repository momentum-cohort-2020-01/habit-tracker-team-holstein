from django.contrib import admin
from .models import Habit, Observer, Record 

# Register your models here.
admin.site.register(Habit)
admin.site.register(Observer)
admin.site.register(Record)

