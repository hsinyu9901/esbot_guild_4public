# Generated by Django 3.0.3 on 2020-08-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esapp', '0008_auto_20200827_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, default='促銷特價', to='esapp.Tag'),
        ),
    ]
