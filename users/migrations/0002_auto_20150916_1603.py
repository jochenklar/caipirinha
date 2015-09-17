# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetailKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField()),
                ('type', models.CharField(max_length=8, choices=[(b'text', b'Input field'), (b'textarea', b'Textarea field'), (b'checkbox', b'Checkbox'), (b'radio', b'Radio button'), (b'select', b'Select field'), (b'multiselect', b'Multiselect field')])),
                ('hint', models.TextField(blank=True)),
                ('options', models.TextField(blank=True)),
                ('required', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='detail',
            name='key',
            field=models.ForeignKey(related_name='details', to='users.DetailKey'),
        ),
        migrations.AddField(
            model_name='detail',
            name='user',
            field=models.ForeignKey(related_name='details', to=settings.AUTH_USER_MODEL),
        ),
    ]
