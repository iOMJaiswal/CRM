# Generated by Django 4.2.11 on 2024-04-24 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='id',
            new_name='uuid',
        ),
    ]