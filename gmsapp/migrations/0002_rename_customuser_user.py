# Generated by Django 4.1 on 2023-11-13 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]
