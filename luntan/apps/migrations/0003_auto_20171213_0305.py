# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20171211_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questioninfo',
            name='q_content',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='questioninfo',
            name='q_title',
            field=models.CharField(max_length=200),
        ),
    ]
