'''module: Model for the Profile
   author: Ronnie Young
'''
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    '''Model for viewing the profile of logged in User
    Arguments:
        models {[user]} -- one to one relationship to profile to access the key
                address -- character field to gather address info
                phone --- integar field for phone number
    '''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey("Schedule", on_delete=models.CASCADE)
