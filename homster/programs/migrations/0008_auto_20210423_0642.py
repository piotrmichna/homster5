# Generated by Django 3.1.7 on 2021-04-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0007_auto_20210423_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progstarttime',
            name='next_start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Następny start'),
        ),
    ]
