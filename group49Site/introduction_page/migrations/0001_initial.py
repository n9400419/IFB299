# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-10 02:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='userRegisterAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('fullname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='userRegisterAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introduction_page.userRegisterAccount'),
        ),
    ]