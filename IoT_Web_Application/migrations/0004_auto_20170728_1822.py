# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_Web_Application', '0003_auto_20170720_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify_txt_users',
            name='NotificationService',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notify_txt_users',
            name='Phone_Number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]