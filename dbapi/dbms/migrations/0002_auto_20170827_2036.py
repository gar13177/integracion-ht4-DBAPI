# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendetalle',
            name='id_orden',
            field=models.ForeignKey(db_column='id_orden', on_delete=django.db.models.deletion.CASCADE, related_name='orden_detalle', to='dbms.Orden'),
        ),
    ]
