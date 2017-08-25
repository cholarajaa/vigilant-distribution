# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 11:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AggregatedUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(blank=True, max_length=256, null=True)),
                ('company', models.CharField(max_length=256)),
                ('usertype', models.CharField(max_length=256)),
                ('lowTemp', models.FloatField(blank=True, null=True)),
                ('referenceTemp', models.FloatField(blank=True, null=True)),
                ('referenceLife', models.FloatField(blank=True, null=True)),
                ('partnerName', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('segmentTypeDeparture', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('functionalName', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('partnerTypeStart', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('bizLocationTypeStart', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('packagingTypeCode', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('tradeItemCountryOfOrigin', django.contrib.postgres.fields.jsonb.JSONField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('organization_id', models.IntegerField()),
                ('raspberry_id', models.CharField(max_length=256)),
                ('event_type', models.CharField(max_length=256)),
                ('event_order', models.IntegerField()),
                ('is_current', models.BooleanField()),
                ('elapsed_seconds', models.IntegerField()),
                ('company_name', models.CharField(blank=True, max_length=256, null=True)),
                ('client', models.CharField(blank=True, max_length=256, null=True)),
                ('read_point', models.CharField(blank=True, max_length=256, null=True)),
                ('biz_location', models.CharField(blank=True, max_length=256, null=True)),
                ('biz_step', models.CharField(blank=True, max_length=256, null=True)),
                ('version', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventsDump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events_json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=256)),
                ('company', models.CharField(max_length=256)),
                ('usertype', models.CharField(max_length=256)),
                ('partnerName', models.CharField(blank=True, max_length=256, null=True)),
                ('segmentTypeDeparture', models.CharField(blank=True, max_length=256, null=True)),
                ('functionalName', models.CharField(blank=True, max_length=256, null=True)),
                ('partnerTypeStart', models.CharField(blank=True, max_length=256, null=True)),
                ('bizLocationTypeStart', models.CharField(blank=True, max_length=256, null=True)),
                ('packagingTypeCode', models.CharField(blank=True, max_length=256, null=True)),
                ('tradeItemCountryOfOrigin', models.CharField(max_length=256)),
                ('lowTemp', models.IntegerField()),
                ('referenceTemp', models.IntegerField()),
                ('referenceLife', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reactor.Event')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('time', 'organization_id', 'raspberry_id', 'event_type', 'event_order')]),
        ),
        migrations.AlterIndexTogether(
            name='event',
            index_together=set([('time', 'organization_id', 'raspberry_id', 'event_type', 'event_order')]),
        ),
        migrations.AlterUniqueTogether(
            name='aggregateduserdata',
            unique_together=set([('company', 'usertype')]),
        ),
        migrations.AlterUniqueTogether(
            name='userdata',
            unique_together=set([('owner_name', 'company', 'usertype')]),
        ),
        migrations.AlterIndexTogether(
            name='userdata',
            index_together=set([('owner_name', 'company', 'usertype')]),
        ),
    ]
