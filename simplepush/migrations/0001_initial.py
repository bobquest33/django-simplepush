# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PushInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('browser', models.CharField(max_length=100)),
                ('endpoint', models.URLField(max_length=255)),
                ('auth', models.CharField(max_length=100)),
                ('p256dh', models.CharField(max_length=100)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='pushinformation',
            name='subscription',
            field=models.ForeignKey(to='simplepush.SubscriptionInfo'),
        ),
        migrations.AddField(
            model_name='pushinformation',
            name='user',
            field=models.ForeignKey(related_name='simplepush_info', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
