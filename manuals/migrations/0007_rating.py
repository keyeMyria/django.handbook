# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0006_comment_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.PositiveIntegerField(default=0)),
                ('total', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
