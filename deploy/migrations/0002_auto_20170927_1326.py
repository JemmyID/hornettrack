# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footprint',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='deploy.Creeper'),
        ),
    ]
