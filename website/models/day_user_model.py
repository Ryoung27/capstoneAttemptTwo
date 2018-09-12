from django.contrib.auth.models import User
from django.db import models

"""
    module: user_model
    author: Ronnie Young
    purpose: To create the data model for a user and day join table
"""


class Day_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey("Day", on_delete=models.CASCADE)
    thoughts = models.TextField(blank=True, max_length=500)
    time = models.IntegerField()
    def __str__(self):
        return self.user.username
# # I really need to speak to them about passwords on Tuesday