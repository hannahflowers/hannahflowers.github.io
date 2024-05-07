# Generated by Django 5.0.4 on 2024-05-06 13:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floral_jamming', '0015_remove_attendee_email_remove_attendee_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='floral_jamming.event'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to=settings.AUTH_USER_MODEL),
        ),
    ]