# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('a_content', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('q_title', models.CharField(max_length=20)),
                ('q_content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('user_pwd', models.CharField(max_length=20)),
                ('user_email', models.CharField(default='', max_length=50)),
                ('nickname', models.CharField(default='', max_length=20)),
                ('user_avatar', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='questioninfo',
            name='q_user',
            field=models.ForeignKey(to='apps.UserInfo'),
        ),
        migrations.AddField(
            model_name='answerinfo',
            name='a_question',
            field=models.ForeignKey(to='apps.QuestionInfo'),
        ),
        migrations.AddField(
            model_name='answerinfo',
            name='a_user',
            field=models.ForeignKey(to='apps.UserInfo'),
        ),
    ]
