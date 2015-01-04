# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikesurvey', '0005_auto_20150103_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biker',
            name='bikerGender',
            field=models.CharField(default=None, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
