# Generated by Django 5.1.2 on 2024-10-29 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estaciones',
            old_name='ubicaion',
            new_name='ubicacion',
        ),
    ]
