# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bikesurvey', '0002_biker_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biker',
            name='count',
        ),
        migrations.AddField(
            model_name='biker',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='biker',
            name='bikerGender',
            field=models.CharField(max_length=1, choices=[(b'M', b'M'), (b'F', b'F')]),
        ),
        migrations.AlterField(
            model_name='biker',
            name='bikerHelmet',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='biker',
            name='bikerLocation',
            field=models.CharField(max_length=30, choices=[(b'Sidewalk', b'Sidewalk'), (b'Street', b'Street')]),
        ),
        migrations.AlterField(
            model_name='surveyinstance',
            name='location',
            field=models.CharField(max_length=200, choices=[(b'Regents Drive @ Rt. 1', b'Regents Drive @ Rt. 1'), (b'Mowatt Lane Garage Exit @ Knox Rd.', b'Mowatt Lane Garage Exit @ Knox Rd.'), (b'Mall @ Woods Hall', b'Mall @ Woods Hall'), (b'Regents Dr. @ Main Administration', b'Regents Dr. @ Main Administration'), (b'Campus Dr. @ Paint Branch Dr.', b'Campus Dr. @ Paint Branch Dr.'), (b'Campus Dr. @ The Stamp', b'Campus Dr. @ The Stamp'), (b'Regents Drive @ Stadium Drive', b'Regents Drive @ Stadium Drive'), (b'Paint Branch Drive @ Lot 11b', b'Paint Branch Drive @ Lot 11b'), (b'Campus Drive @ Adelphi Road', b'Campus Drive @ Adelphi Road')]),
        ),
        migrations.AlterField(
            model_name='surveyinstance',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
