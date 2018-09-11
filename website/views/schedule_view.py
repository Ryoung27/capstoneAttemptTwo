# from rest_framework import viewsets
# from website import models


# class Schedule_Viewset(viewsets.ModelViewSet):
#     queryset = models.Schedule.objects.all()


from django.shortcuts import render
from website.models import Schedule, Day, Profile
# from django.contrib.auth.models import User

def schedule_view(request):
    """View for the day

    Arguments:
        GET, returns render of template with information.
    """
    current_user = request.user
    #profile = Profile.objects.all()
    print(current_user.id)
    profile = Profile.objects.filter(user_id = current_user.id)


    # print(user_schedule[0])

    user_schedule = Schedule.objects.filter(id = profile[0].schedule_id)
    print(user_schedule)
    day_schedule = Day.objects.filter(schedule = user_schedule[0])

    # new_day_schedule = day_schedule(pk=id)
    # print(day_schedule)

    #perform the logic
    # current_schedule = next((schedule for schedule in user_schedule if schedule.user_id == User.id), User.id)

    if request.method == "GET":
        # schedule = Schedule.objects.all()
        return render(request, 'run/schedule.html', {"schedules": user_schedule, "days": day_schedule})

    #Place holder text.
    # schedule = Schedule.objects.all()
    # return render(request, 'run/schedule.html', {})
    # if request.method == "GET":
    #     day = Day.objects.all()
    #     data_set = []
    #     for day in days:
    #         #Need to work on this if function.
    #         #Based on Levi's category_view.py

    #     template_name= "website/day.html"
    #     return render(request, template_name, {'data_set':data_set})