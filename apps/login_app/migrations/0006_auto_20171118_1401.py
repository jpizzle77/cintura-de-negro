# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-18 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0005_auto_20171118_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(),
        ),
    ]
