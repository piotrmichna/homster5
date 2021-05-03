# Generated by Django 3.1.7 on 2021-05-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20210504_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherlong',
            name='humi_day_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, verbose_name='Wilgotność powietrza'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='humi_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, verbose_name='Wilgotność powietrza'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='humi_night_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, verbose_name='Wilgotność powietrza'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='ligh_day_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=7, verbose_name='Nasłonecznienie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='ligh_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=7, verbose_name='Nasłonecznienie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='ligh_night_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, verbose_name='Nasłonecznienie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='pres_day_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='Ciśnienie atmosferyczne'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='pres_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='Ciśnienie atmosferyczne'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='pres_night_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='Ciśnienie atmosferyczne'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='temp_day_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, verbose_name='Temperatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='temp_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, verbose_name='Temperatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='temp_night_m',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, verbose_name='Temperatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='time_day',
            field=models.TimeField(default='00:00:00', verbose_name='Długość dnia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='time_day_start',
            field=models.TimeField(default='00:00:00', verbose_name='Czas rozpoczęcia dnia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherlong',
            name='time_day_stop',
            field=models.TimeField(default='00:00:00', verbose_name='Czas zakończenia dnia'),
            preserve_default=False,
        ),
    ]
