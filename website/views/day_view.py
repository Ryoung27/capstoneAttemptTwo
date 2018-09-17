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
    day = get_object_or_404(Day, pk=pk)
    if request.method == "GET":
        # day = get_object_or_404(Day, pk=pk)

        user_day= Day_User.objects.filter(day=day.id, user=request.user)
        if user_day:
            user_day= Day_User.objects.get(day=day.id, user=request.user)
            # user_day[0]
            time = Day_User.objects.filter(day_id=day.id)[0].time
            Day_Form = DayForm()
            return render(request, 'run/day.html', {"day":day, "user_day": user_day, "time": time, "Day_Form": Day_Form})
        else:
            Day_Form = DayForm()
            return render(request, "run/day.html", {"day":day, "Day_Form": Day_Form} )


  #This needs to post to the join table of website_day_user
    elif request.method == "POST":
       form = DayForm(request.POST)
       form.data = request.POST
       joinForm = form.save(commit=False)
       joinForm.user = request.user
       joinForm.day = day
       joinForm.save()
       return  HttpResponseRedirect(reverse('website:day_view', args=[pk]))


