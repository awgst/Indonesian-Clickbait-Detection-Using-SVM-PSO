# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataCek',
            fields=[
                ('id_cek', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.DateField()),
                ('konten', models.TextField(blank=True, null=True)),
                ('preprocessing', models.TextField(blank=True, null=True)),
                ('tfidf', models.TextField(blank=True, null=True)),
                ('klasifikasi', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'cek_clickbait',
            },
        ),
    ]
