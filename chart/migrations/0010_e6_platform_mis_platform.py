# Generated by Django 4.0 on 2022-09-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0009_rename_failurae_rate_area_claim_frequency_failure_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='e6_platform_mis',
            name='platform',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='平台'),
        ),
    ]
