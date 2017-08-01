from django import forms

from .models import Notify_txt_Users


class NewNotificationRecipient(forms.ModelForm):

    class Meta:
        model = Notify_txt_Users
        fields = ['First_Name', 'Last_Name', 'Phone_Number', 'Email', 'NotificationService', ]
