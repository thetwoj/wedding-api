# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('offered_plus_one', models.BooleanField(default=False)),
                ('bringing_plus_one', models.BooleanField(default=False)),
                ('attending', models.NullBooleanField(default=None)),
                ('food_choice', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sent', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('access_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='invitation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='restapi.Invitation'),
        ),
    ]
