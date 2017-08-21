# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 13:05
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactor', '0003_auto_20170821_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='aggregateduserdata',
            name='bizLocationTypeStart',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='aggregateduserdata',
            name='functionalName',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='aggregateduserdata',
            name='packagingTypeCode',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='aggregateduserdata',
            name='partnerName',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='aggregateduserdata',
            name='partnerTypeStart',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='aggregateduserdata',
            name='segmentTypeDeparture',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='aggregateduserdata',
            name='tradeItemCountryOfOrigin',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
    ]