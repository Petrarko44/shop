# Generated by Django 4.2.13 on 2024-06-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_initial'),
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
            name='username',
        ),
        migrations.AlterField(
            model_name='newuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='detail_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]