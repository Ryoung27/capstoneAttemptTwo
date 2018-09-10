from django.db import models
from .schedule_model import Schedule
# from .user_model import User
from django.contrib.auth.models import User

"""
    module: Day Model
    author: Ronnie Young
    purpose: To create the data model for a day.
"""


class Day(models.Model):
    schedule = models.ManyToManyField('Schedule')
    distance = models.CharField(max_length=10)
    user = models.ManyToManyField(User)
    thoughts = models.TextField(blank=True, max_length=500)
    time = models.IntegerField()