# Generated by Django 3.0.3 on 2020-08-21 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esapp', '0003_auto_20200821_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='member',
        ),
    ]
