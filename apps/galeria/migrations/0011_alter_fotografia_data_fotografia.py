# Generated by Django 5.0.6 on 2024-06-10 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0010_alter_fotografia_data_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
