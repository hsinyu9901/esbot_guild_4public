# Generated by Django 3.0.3 on 2020-08-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esapp', '0006_auto_20200827_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
