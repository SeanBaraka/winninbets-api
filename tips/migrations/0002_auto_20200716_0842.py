# Generated by Django 3.0.8 on 2020-07-16 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tip',
            name='odds',
        ),
        migrations.AlterModelTable(
            name='tip',
            table='tips',
        ),
    ]