# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikesurvey', '0004_auto_20150103_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biker',
            name='bikerGender',
            field=models.CharField(default=None, max_length=1, choices=[(b'M', b'M'), (b'F', b'F')]),
        ),
        migrations.AlterField(
            model_name='biker',
            name='bikerHelmet',
            field=models.CharField(default=None, max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AlterField(
            model_name='biker',
            name='bikerLocation',
            field=models.CharField(default=None, max_length=30, choices=[(b'Sidewalk', b'Sidewalk'), (b'Street', b'Street')]),
        ),
    ]
