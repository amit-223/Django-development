# Generated by Django 5.1.4 on 2025-01-29 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='picture',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='rating',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
