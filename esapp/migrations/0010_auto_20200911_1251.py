# Generated by Django 3.0.3 on 2020-09-11 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esapp', '0009_auto_20200827_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='esapp.Producer'),
        ),
    ]