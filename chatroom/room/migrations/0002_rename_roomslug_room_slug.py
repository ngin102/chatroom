# Generated by Django 4.2.3 on 2023-07-09 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='roomSlug',
            new_name='slug',
        ),
    ]
