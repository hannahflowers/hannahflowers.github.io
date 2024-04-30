# Generated by Django 5.0.4 on 2024-04-30 12:21

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floral_jamming', '0005_session_price_alter_session_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=80, validators=[django.core.validators.MinValueValidator(0)])),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=3000)),
                ('capacity', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='attendee',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='floral_jamming.event'),
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]
