# Generated by Django 3.1.7 on 2021-04-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0017_auto_20210423_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progstarttime',
            name='next_time',
            field=models.DateTimeField(default='2021-04-23T19:40:02.111516', verbose_name='Następny start'),
        ),
    ]
