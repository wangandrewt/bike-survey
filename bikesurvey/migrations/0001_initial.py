# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bikerGender', models.CharField(default=None, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('bikerHelmet', models.CharField(default=None, max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('bikerLocation', models.CharField(default=None, max_length=30, choices=[(b'Sidewalk', b'Sidewalk'), (b'Street', b'Street')])),
                ('time', models.TimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurveyInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200, choices=[(b'Regents Drive @ Rt. 1', b'Regents Drive @ Rt. 1'), (b'Mowatt Lane Garage Exit @ Knox Rd.', b'Mowatt Lane Garage Exit @ Knox Rd.'), (b'Mall @ Woods Hall', b'Mall @ Woods Hall'), (b'Regents Dr. @ Main Administration', b'Regents Dr. @ Main Administration'), (b'Campus Dr. @ Paint Branch Dr.', b'Campus Dr. @ Paint Branch Dr.'), (b'Campus Dr. @ The Stamp', b'Campus Dr. @ The Stamp'), (b'Regents Drive @ Stadium Drive', b'Regents Drive @ Stadium Drive'), (b'Paint Branch Drive @ Lot 11b', b'Paint Branch Drive @ Lot 11b'), (b'Campus Drive @ Adelphi Road', b'Campus Drive @ Adelphi Road')])),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='biker',
            name='surveyInstance',
            field=models.ForeignKey(to='bikesurvey.SurveyInstance'),
            preserve_default=True,
        ),
    ]
