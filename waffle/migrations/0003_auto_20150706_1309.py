# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waffle', '0002_auto_20150617_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='sites',
            field=models.ManyToManyField(
                default=None, to='sites.Site', blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sites',
            field=models.ManyToManyField(
                default=None, to='sites.Site', blank=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='sites',
            field=models.ManyToManyField(
                default=None, to='sites.Site', blank=True),
        ),
    ]
