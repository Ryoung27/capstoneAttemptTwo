"""module: Profile form and Profile Update Form
   author: Ronnie Young
"""



from django.contrib.auth.models import User
from django import forms

from website.models import Profile

'''Form for user fields as well as the address and phone fields for profile'''
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('schedule',)
'''Form for updating the Profile and User'''
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('schedule',)