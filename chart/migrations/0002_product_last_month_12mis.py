# Generated by Django 4.0 on 2022-09-01 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_last_month_12mis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_line', models.CharField(max_length=255, verbose_name='产品名称')),
                ('mis_data', models.IntegerField(verbose_name='最近月')),
                ('mis_12', models.DecimalField(decimal_places=1, max_digits=24, verbose_name='12mis的值')),
            ],
            options={
                'db_table': 'Product_last_month_12mis',
            },
        ),
    ]
