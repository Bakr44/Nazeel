# Generated by Django 4.1.7 on 2023-06-20 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0003_alter_mainservice_time_off_alter_mainservice_time_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainservice',
            name='time_off',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 20, 11, 59, 9, 928217, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='time_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 20, 11, 59, 9, 928217, tzinfo=datetime.timezone.utc)),
        ),
    ]
