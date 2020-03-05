from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=100)
    goal = models.IntegerField()
    unit = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"Activity {self.name} Target-Goal {self.goal} Unit {self.unit}"


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True, null=True)
    achievement = models.PositiveIntegerField(default=0)
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name='records', blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='records', blank=True, null=True)

    def __str__(self): 
        return f"{self.owner.username}'s {self.habit.name} on {self.date}"

    class Meta:
        constraints = [models.UniqueConstraint(fields=['date', 'habit', 'owner'], name='unique_record')]


class Observer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='observations', blank=True, null=True)
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name='observers', blank=True, null=True)

    def __str__(self):
        return f"User: {self.user.pk} watches Habit: {self.habit.pk}"
   