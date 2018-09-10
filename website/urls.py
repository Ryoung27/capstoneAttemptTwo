from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^day_view/(?P<pk>\d+)/$', views.day_view, name='day_view'),
    url(r'schedule_view$', views.schedule_view, name='schedule_view'),
]

