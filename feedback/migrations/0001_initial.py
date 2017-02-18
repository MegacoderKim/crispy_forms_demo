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
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=5, choices=[(b'one', b'1'), (b'two', b'2'), (b'three', b'3'), (b'four', b'4'), (b'five', b'5')])),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Neighbour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='neighbourhoods',
            field=models.ForeignKey(related_name='neighbours', to='feedback.Neighbour'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_name',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
