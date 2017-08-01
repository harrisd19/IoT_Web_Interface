from django.conf.urls import url
from . import views

app_name = 'IoTWiFi'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^advanced/$', views.advancedsetup, name='advancedsetup'),
    url(r'^SMSindex/$', views.SMS, name='SMSindex'),
    url(r'^SMSindex/New_Time_Based/$', views.TimeBasedCreate, name='add_timebased'),
    url(r'^SMSindex/New_Instant/$', views.add_instant, name='add_instant'),
]
