# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20151025_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('details', jsonfield.fields.JSONField()),
                ('user', models.ForeignKey(related_name='details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='detail',
            name='key',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
