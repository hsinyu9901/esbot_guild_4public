# Generated by Django 3.0.3 on 2020-08-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esapp', '0005_remove_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, default='促銷特價', null=True, to='esapp.Tag'),
        ),
    ]
