# Generated by Django 4.2.2 on 2023-06-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0003_alter_mainservice_time_off_alter_mainservice_time_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainservice',
            name='time_off',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='time_on',
            field=models.DateTimeField(),
        ),
    ]