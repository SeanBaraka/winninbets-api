# Generated by Django 3.0.8 on 2020-07-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customer_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='vip_expiry',
            field=models.DateField(null=True),
        ),
    ]
