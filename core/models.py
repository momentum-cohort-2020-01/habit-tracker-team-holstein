from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=100)
    goal = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"Activity {self.name} Target-Goal {self.goal}"
   