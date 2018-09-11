from django import forms
from website.models import Day_User

class DayForm(forms.ModelForm):

    class Meta:
        model = Day_User
        fields = ('thoughts', 'time')
