from django import forms
from website.models import Day

class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('thoughts', 'time')
