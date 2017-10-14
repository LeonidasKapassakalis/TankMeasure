# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-10 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tank_Measurement', '0006_auto_20170910_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sftable',
            options={'ordering': ('id', 'sftprodid')},
        ),
        migrations.RemoveField(
            model_name='sftable',
            name='sftprod',
        ),
        migrations.AddField(
            model_name='sftable',
            name='sftprodid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Tank_Measurement.Kausima', verbose_name='Kausima'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='sftable',
            table=None,
        ),
    ]
