from django.shortcuts import render

# This is the basic user view model.
# it just takes in the user information and returns it.
def user_view(request):
    """View for the day

    Arguments:
        GET, returns render of template with information.
    """
    user = User.objects.all()
    return render(request, template_name, {'data_set':data_set})
