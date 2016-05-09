# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default='a', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
