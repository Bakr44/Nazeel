# Generated by Django 4.1.7 on 2023-06-15 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_app', '0003_remove_guest_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='number',
            new_name='room_number',
        ),
    ]