# Generated by Django 3.2.5 on 2021-10-15 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_blogdb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blogdb',
            new_name='blog',
        ),
    ]
