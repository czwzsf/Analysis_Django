from django.db import models


# Create your models here.

# 数字化大屏数据来源

class bottomLeftChart(models.Model):
    category = models.CharField(max_length=128, verbose_name="地区名称")
    lineData = models.BigIntegerField(verbose_name="计划贯通")
    barData = models.BigIntegerField(verbose_name="实际贯通")

    class Meta:
        db_table = 'bottomLeftChart'
