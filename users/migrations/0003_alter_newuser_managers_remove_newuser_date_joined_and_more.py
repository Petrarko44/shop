# Generated by Django 4.2.13 on 2024-06-05 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_table'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='newuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='username',
        ),
    ]
