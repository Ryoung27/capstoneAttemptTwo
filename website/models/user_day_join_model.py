from django.db import models
from django.contrib.auth.models import User



"""
    module: User_Day_Join Model
    author: Ronnie Young
    purpose: To create the data model for a user day join table.
"""


class Day_Join_Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey('Day', on_delete=models.CASCADE)
    thoughts = models.CharField(max_length=1000)
    time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)