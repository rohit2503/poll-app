# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='polls.Questions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='questions',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 7, 39, 1, 231909), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_text',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
