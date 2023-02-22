# Generated by Django 4.1.7 on 2023-02-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='totalprice',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='shopstore',
            name='productcode',
            field=models.CharField(default=4300353, max_length=10, unique=True),
        ),
    ]
