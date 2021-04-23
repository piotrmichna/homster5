# Generated by Django 3.1.7 on 2021-04-23 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0011_auto_20210423_0804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progpincfg',
            old_name='enabled',
            new_name='active',
        ),
        migrations.AddField(
            model_name='progpincfg',
            name='stop_time',
            field=models.TimeField(default='18:58:30', verbose_name='Czas zakończenia działania'),
        ),
        migrations.AddField(
            model_name='progstarttime',
            name='running',
            field=models.BooleanField(default=False, verbose_name='Uruchomiony'),
        ),
        migrations.AlterField(
            model_name='progstarttime',
            name='next_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 18, 58, 30, 487223), verbose_name='Następny start'),
        ),
    ]
