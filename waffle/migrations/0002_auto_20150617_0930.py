# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='sites',
            field=models.ManyToManyField(default=None, to='sites.Site', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sample',
            name='sites',
            field=models.ManyToManyField(default=None, to='sites.Site', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='switch',
            name='sites',
            field=models.ManyToManyField(default=None, to='sites.Site', null=True, blank=True),
            preserve_default=True,
        ),
    ]
