# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170213_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=90, unique=settings.PINAX_BLOG_SLUG_UNIQUE, verbose_name='Slug'),
        ),
    ]