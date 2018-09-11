# from rest_framework import viewsets
# from website import models


# class Day_Viewset(viewsets.ModelViewSet):
#     queryset = models.Day.objects.all()

from django.shortcuts import render, get_object_or_404
from website.models import Day, Schedule, Day_User
from website.forms import DayForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def day_view(request, pk):
    """View for the day

    Arguments:
        GET, returns render of template with information.
    """
    #Currently converting Day to Day_User
    if request.method == "GET":
        day = get_object_or_404(Day, pk=pk)
        thoughts = Day.objects.filter(id = day.id)[0].thoughts
        time = Day.objects.filter(id = day.id)[0].time
        Day_Form = DayForm()
        return render(request, 'run/day.html', {"day":day, "thoughts": thoughts, "time": time, "Day_Form": Day_Form})
    # Next hellzone. I need Kimmy or Joe's help with this.
    # elif request.method == "POST":
    #     data = Day_Join_Table(
    #         user = request.user.id ,
    #         day = request.Day.id,
    #         time = request.POST['time'] ,
    #         thoughts = request.POST['thoughts'],
    #     )
    #     form = DayForm(data=request.POST, files=request.FILES, instance = data)
    #     form.save()
    #Opition to hellzone.
    elif request.method == "POST":
       form = DayForm(request.POST)
       form.data = request.POST
       form.save()
       return  HttpResponseRedirect(reverse('website:day_view', args=(pk)))



#Change ERD completely.