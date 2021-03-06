# Generated by Django 3.0.3 on 2020-08-21 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer_name', models.CharField(max_length=200, null=True)),
                ('producer_ctiy', models.CharField(choices=[('基隆市', '基隆市'), ('台北市', '台北市'), ('新北市', '新北市'), ('桃園縣', '桃園縣'), ('新竹市', '新竹市'), ('新竹縣', '新竹縣'), ('苗栗縣', '苗栗縣'), ('台中市', '台中市'), ('彰化縣', '彰化縣'), ('南投縣', '南投縣'), ('雲林縣', '雲林縣'), ('嘉義市', '嘉義市'), ('嘉義縣', '嘉義縣'), ('台南市', '台南市'), ('高雄市', '高雄市'), ('屏東縣', '屏東縣'), ('台東縣', '台東縣'), ('花蓮縣', '花蓮縣'), ('宜蘭縣', '宜蘭縣'), ('澎湖縣', '澎湖縣'), ('金門縣', '金門縣'), ('連江縣', '連江縣')], max_length=20, null=True)),
                ('producer_address', models.CharField(max_length=500, null=True)),
                ('producer_time', models.CharField(blank=True, default='-', max_length=50, null=True)),
                ('producer_email', models.EmailField(max_length=200, null=True)),
                ('producer_phone', models.CharField(max_length=20, null=True)),
                ('producer_info', models.TextField(blank=True, max_length=500, null=True)),
                ('charge', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='esapp.Friend')),
            ],
        ),
    ]
