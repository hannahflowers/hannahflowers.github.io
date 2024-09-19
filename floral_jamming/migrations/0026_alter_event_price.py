# Generated by Django 5.0.4 on 2024-09-19 07:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floral_jamming', '0025_attendee_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]