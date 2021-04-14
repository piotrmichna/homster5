# Generated by Django 3.1.7 on 2021-04-14 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CfgType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Komenda')),
                ('description', models.CharField(max_length=128, null=True, verbose_name='Opis polecenia')),
            ],
            options={
                'verbose_name': 'Typ komendy',
                'verbose_name_plural': 'Typy komend',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CfgCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Komenda')),
                ('value', models.CharField(max_length=16, verbose_name='Wartość')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.cfgtype', verbose_name='Typ komendy')),
            ],
            options={
                'verbose_name': 'Konfiguracja',
                'verbose_name_plural': 'Konfiguracja - komendy',
                'ordering': ['name'],
            },
        ),
    ]
