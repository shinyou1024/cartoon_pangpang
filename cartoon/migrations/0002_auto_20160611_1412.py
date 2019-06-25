# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartoon', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='cartoon',
            name='ct',
        ),
        migrations.RemoveField(
            model_name='cartoon',
            name='ct_title',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='sc_contents',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='sc_num',
        ),
        migrations.AddField(
            model_name='cartoon',
            name='ct_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene',
            name='ct_contents',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]