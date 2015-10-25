# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150916_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='key',
            field=models.ForeignKey(related_name='details', to='users.DetailKey', unique=True),
        ),
        migrations.AlterField(
            model_name='detailkey',
            name='options',
            field=jsonfield.fields.JSONField(),
        ),
    ]
