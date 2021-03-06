# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsvp', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('rsvp_date', models.DateField(default=django.utils.timezone.now)),
                ('meal_preference', models.CharField(choices=[('chicken', 'chicken'), ('veg', 'veg'), ('fish', 'fish')], max_length=50)),
                ('accom_preference', models.CharField(choices=[('hotel', 'Hotel'), ('hut', 'Hut'), ('castle', 'Fish')], max_length=50)),
                ('text', models.TextField(blank=True, default='')),
                ('kid', models.BooleanField(default=False)),
                ('party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rsvp.Guest')),
            ],
        ),
    ]
