# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0002_auto_20170827_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(default='user', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='user', max_length=100),
            preserve_default=False,
        ),
    ]
