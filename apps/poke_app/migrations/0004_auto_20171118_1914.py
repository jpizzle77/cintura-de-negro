# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-19 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke_app', '0003_poke_poke_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poke',
            name='poke_count',
            field=models.IntegerField(),
        ),
    ]
