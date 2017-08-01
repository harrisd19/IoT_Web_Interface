from django.contrib.auth.models import Permission, User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse


class Notify_txt_Users(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=100)
    Phone_Number = PhoneNumberField()
    Email = models.EmailField(max_length=254)
    NotificationService = models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name


class WiFiCredentials(models.Model):
    user = models.CharField(max_length=120)
    SSID = models.CharField(max_length=250)
    Password = models.CharField(max_length=500)

    def __str__(self):
        return self.SSID + ' - ' + self.Password
