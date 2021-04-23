# Generated by Django 3.1.7 on 2021-04-23 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0012_auto_20210423_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progname',
            name='stop_run',
        ),
        migrations.AlterField(
            model_name='progpincfg',
            name='stop_time',
            field=models.TimeField(default='19:37:18', verbose_name='Czas zakończenia działania'),
        ),
        migrations.AlterField(
            model_name='progstarttime',
            name='next_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 19, 37, 18, 173992), verbose_name='Następny start'),
        ),
    ]