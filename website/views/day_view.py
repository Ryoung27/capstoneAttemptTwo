from django.shortcuts import render, get_object_or_404
from website.models import Day, Schedule, Day_User
from website.forms import DayForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# This was the hardest part of designing this code.
# This renders the "day", which is the indivdiual run section.
# Under the calander days.
def day_view(request, pk):
    """View for the day

    Arguments:
        GET, returns render of template with information.
    """
    #Currently converting Day to Day_User
    day = get_object_or_404(Day, pk=pk)
    if request.method == "GET":
        # day = get_object_or_404(Day, pk=pk)
        # this compares the user days to the user id's on the user join table.
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
    # If the method is GET it will go into an if else statement, if there is
    # information in the table for that particular day. It will display it
    # else it is an empty day and gives us a form to add data to the table.

  #This needs to post to the join table of website_day_user
    elif request.method == "POST":
       form = DayForm(request.POST)
       form.data = request.POST
       joinForm = form.save(commit=False)
       joinForm.user = request.user
       joinForm.day = day
       joinForm.save()
       return  HttpResponseRedirect(reverse('website:day_view', args=[pk]))
    # This is the else section of our if statement above. If the data is empty it will allow us to post and update form data.


