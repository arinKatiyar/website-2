# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_remove_gamelink_accepted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelink',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='games.Game'),
        ),
    ]
