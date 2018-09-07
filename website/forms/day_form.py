from django import forms
from website.models import Day_Join_Table

class DayForm(forms.ModelForm):

    class Meta:
        model = Day_Join_Table
        fields = ('thoughts', 'time')
