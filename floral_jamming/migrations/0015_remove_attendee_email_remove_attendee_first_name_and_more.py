# Generated by Django 5.0.4 on 2024-05-06 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floral_jamming', '0014_remove_attendee_guest_id_attendee_guest_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='last_name',
        ),
    ]