# Generated by Django 4.1.7 on 2023-02-24 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashapi', '0003_shopstore_currentquantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopstore',
            name='brand',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerorderproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 8, 30, 53, 117711, tzinfo=datetime.timezone.utc)),
        ),
    ]
