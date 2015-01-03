# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikesurvey', '0003_auto_20150103_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biker',
            name='bikerHelmet',
            field=models.CharField(max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
    ]
