# Generated by Django 5.1.4 on 2024-12-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
            ],
        ),
    ]
