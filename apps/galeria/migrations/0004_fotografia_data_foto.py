# Generated by Django 5.0.6 on 2024-05-28 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_foto',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
