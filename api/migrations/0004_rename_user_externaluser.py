# Generated by Django 4.1.6 on 2023-02-13 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='ExternalUser',
        ),
    ]