from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Notify_txt_Users

from IoT_Web_Application.forms import NewNotificationRecipient


##class TimeBasedCreate(CreateView):
    ##model = Notify_txt_Users
    ##template_name = 'SMS/notify_txt_users_form.html'
   ## fields = ['First_Name', 'Last_Name', 'Phone_Number', 'Email', 'NotificationService']

def TimeBasedCreate(request):
    form = NewNotificationRecipient(request.POST)
    if form.is_valid():
        NewRecipient = form.save(commit=False)
        NewRecipient.First_Name = request.First_Name
        NewRecipient.Last_Name = request.Last_Name
        NewRecipient.Phone_Number = request.Phone_Number
        NewRecipient.Email = request.Email
        NewRecipient.NotificationService = request.NotificationService
        NewRecipient.save()
        return render(request, 'SMS/tables-datatablecopy.html')
    return render(request, 'SMS/Add_Timebased.html')



def index(request):

    return render(request, 'WifiConnect/login.html')


def advancedsetup(request):
    return render(request, 'WifiConnect/advancedsetup.html')


def add_instant(request):
    return render(request, 'SMS/Add_Instant.html')


def add_timebased(request):
    return render(request, 'SMS/Add_Timebased.html')


def SMS(request):
    entries = Notify_txt_Users.objects.all()

    args = {'entries': entries}
    return render(request, 'SMS/tables-datatablecopy.html', args)


