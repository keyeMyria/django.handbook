# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 08:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetCode',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='code')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignupCode',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='code')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ipaddr', models.GenericIPAddressField(verbose_name='ip address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
