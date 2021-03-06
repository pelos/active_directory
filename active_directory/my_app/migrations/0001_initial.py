# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.EmailField(max_length=100)),
                ('email2', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.EmailField(max_length=100)),
                ('phone2', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='phones',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.User'),
        ),
        migrations.AddField(
            model_name='emails',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.User'),
        ),
    ]
