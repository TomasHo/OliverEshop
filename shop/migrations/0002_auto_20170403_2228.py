# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkty'},
        ),
    ]
