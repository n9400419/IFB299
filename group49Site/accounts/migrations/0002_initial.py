# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-03 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Businussman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('userType', models.CharField(max_length=11)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('userType', models.CharField(max_length=11)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('userType', models.CharField(max_length=11)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
