# Generated by Django 4.0 on 2022-08-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bottomLeftChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=128, verbose_name='地区名称')),
                ('lineData', models.BigIntegerField(verbose_name='计划贯通')),
                ('barData', models.BigIntegerField(verbose_name='实际贯通')),
            ],
            options={
                'db_table': 'bottomLeftChart',
            },
        ),
    ]
