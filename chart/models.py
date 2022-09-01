from django.db import models


# Create your models here.

# 数字化大屏数据来源

class bottomLeftChart(models.Model):
    category = models.CharField(max_length=128, verbose_name="地区名称")
    lineData = models.BigIntegerField(verbose_name="计划贯通")
    barData = models.BigIntegerField(verbose_name="实际贯通")

    class Meta:
        db_table = 'bottomLeftChart'


class Product_last_month_12mis(models.Model):
    product_line = models.CharField(max_length=255, verbose_name="产品名称")
    mis_data = models.IntegerField(verbose_name="最近月")
    mis_12 = models.DecimalField(max_length=24, verbose_name="12mis的值")
