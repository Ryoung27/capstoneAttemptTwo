# from django.shortcuts import render
# from website.models import Day, Day_Join_Table

# def Day_Join_Table(request):
#     #Getting the current user, it is apperently pulled down naturally in Django.
#     current_user = request.user

#     #A section for any logic I want to use
#     if request.method == "POST":
#         data = Day_Join_Table(
#             user = request.user,
#             day = request.day,
#             thoughts = request.POST['thoughts'],
#             time = request.POST['time']
#         )
#         form = day_form(data=request.POST, files=request.Files, instance=data)
#         form.save()

