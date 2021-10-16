# Generated by Django 3.2.5 on 2021-10-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_doctor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_patient',
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name='Is customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Is employee'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]