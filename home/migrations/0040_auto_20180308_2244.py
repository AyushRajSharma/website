# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-08 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20180221_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantapproval',
            name='self_identify',
            field=models.CharField(blank=True, help_text='If your gender identity is NOT listed above, what is your gender identity?', max_length=100),
        ),
    ]
