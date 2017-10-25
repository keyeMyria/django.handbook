# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 10:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0002_auto_20171025_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manual',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manuals', to=settings.AUTH_USER_MODEL),
        ),
    ]