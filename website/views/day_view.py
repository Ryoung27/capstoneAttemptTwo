# from rest_framework import viewsets
# from website import models


# class Day_Viewset(viewsets.ModelViewSet):
#     queryset = models.Day.objects.all()

from django.shortcuts import render, get_object_or_404
from website.models import Day
from website.forms import DayForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def day_view(request, pk):
    """View for the day

    Arguments:
        GET, returns render of template with information.
    """
    #Place holder text.
    #This is the start of hell
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


# if request.method == ‘GET’:
#        report_form = ReportForm()
#        template_name = ‘createreport.html’
#        return render(request, template_name, {‘report_form’: report_form})

    # if request.method == "GET":
    #     day = Day.objects.all()
    #     data_set = []
    #     for day in days:
    #         #Need to work on this if function.
    #         #Based on Levi's category_view.py

    #     template_name= "website/day.html"
    #     return render(request, template_name, {'data_set':data_set})

#detailed dayview

#   user_schedule = Schedule.objects.filter(user_id = current_user.id)
#   day_schedul se = Day.objects.filter(schedule = user_schedule[0])

# thoughts = Day_Join_Table.objects.filter(day_id = day.id)
#     print(thoughts[0].thoughts)