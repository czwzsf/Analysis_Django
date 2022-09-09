# Generated by Django 4.0 on 2022-09-09 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0004_product_id_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_station_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=128, verbose_name='服务站名称')),
                ('claimfrequency', models.IntegerField(verbose_name='索赔频次')),
                ('date_month', models.DateTimeField(verbose_name='索赔年月')),
                ('type_car', models.CharField(max_length=16, verbose_name='车型')),
                ('engine_platform', models.CharField(max_length=64, verbose_name='发动机平台')),
                ('car_let', models.CharField(max_length=32, verbose_name='排放')),
                ('purpose', models.CharField(max_length=64, verbose_name='用途')),
            ],
        ),
    ]