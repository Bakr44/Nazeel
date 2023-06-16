# Generated by Django 4.1.7 on 2023-06-15 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guest_app', '0005_guest_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='room',
        ),
        migrations.AlterField(
            model_name='guest',
            name='room_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest_app.room'),
        ),
    ]
