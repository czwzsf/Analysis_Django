# Generated by Django 4.0 on 2022-09-14 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0007_area_claim_frequency_e6_platform_mis_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part_claim_mis',
            old_name='chain_ration',
            new_name='chain_ratio',
        ),
    ]
