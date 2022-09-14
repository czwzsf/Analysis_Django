from django.db import models


# Create your models here.

# 数字化大屏数据来源

class Product_id(models.Model):
    # 产品id
    product_id = models.IntegerField(verbose_name="产品id")
    product_name = models.CharField(max_length=128, verbose_name="产品名称", blank=True, null=True)

    class Meta:
        db_table = 'Product_id'


class bottomLeftChart(models.Model):
    category = models.CharField(max_length=128, verbose_name="地区名称")
    lineData = models.BigIntegerField(verbose_name="计划贯通")
    barData = models.BigIntegerField(verbose_name="实际贯通")

    class Meta:
        db_table = 'bottomLeftChart'


class Product_last_month_12mis(models.Model):
    # 产品最近月12mis
    product_line = models.CharField(max_length=255, verbose_name="产品名称")
    mis_data = models.IntegerField(verbose_name="最近月")
    mis_12 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="12mis的值")
    product_id = models.ForeignKey(Product_id, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'Product_last_month_12mis'


class Service_station_information(models.Model):
    # 服务站索赔频次
    station_name = models.CharField(max_length=128, verbose_name="服务站名称")
    claimfrequency = models.IntegerField(verbose_name="索赔频次")
    date_month = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="索赔年月")
    type_car = models.CharField(max_length=16, verbose_name="车型")
    engine_platform = models.CharField(max_length=64, verbose_name="发动机平台")
    car_let = models.CharField(max_length=32, verbose_name="排放")
    purpose = models.CharField(max_length=64, verbose_name="用途")

    class Meta:
        db_table = "Service_station_information"


class platform_information(models.Model):
    # 平台信息
    platform = models.CharField(max_length=128, verbose_name="平台")

    class Meta:
        db_table = "platform_information"


class let_information(models.Model):
    # 排放信息
    let = models.CharField(max_length=128, verbose_name="排放")

    class Meta:
        db_table = "let_information"


class E6_platform_mis(models.Model):
    data_mis = models.CharField(max_length=128, verbose_name="日期")
    mis_12 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="12mis的值")
    mis_9 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="9mis的值")
    mis_6 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="6mis的值")
    mis_3 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="3mis的值")
    platform = models.CharField(max_length=64, verbose_name="平台", null=True, blank=True)

    class Meta:
        db_table = "E6_platform_mis"


class area_claim_frequency(models.Model):
    area = models.CharField(max_length=128, verbose_name="大区地址")
    frequency = models.IntegerField(verbose_name="索赔频次")
    ownership = models.IntegerField(verbose_name="地区拥有量")
    failure_rate = models.CharField(max_length=32, verbose_name="索赔率")
    Date_of_claim = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="索赔年月")
    car_type = models.CharField(max_length=32, verbose_name="车型")
    platform = models.CharField(max_length=64, verbose_name="平台")
    let = models.CharField(max_length=32, verbose_name="排放")
    purpose = models.CharField(max_length=32, verbose_name="用途")

    class Meta:
        db_table = "area_claim_frequency"


class part_claim_mis(models.Model):
    part_name = models.CharField(max_length=128, verbose_name="零部件名称")
    date = models.CharField(max_length=128, verbose_name="日期")
    base_value = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="基础值")
    current_value = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="当前值")
    chain_ratio = models.CharField(max_length=32, verbose_name="环比")
    year_on_year = models.CharField(max_length=32, verbose_name="同比")

    class Meta:
        db_table = "part_claim_mis"


# TODO 未来要使用相关链接来显示，不需要单独创建一个数据库
class mis12_platform_6DM(models.Model):
    platform = models.CharField(max_length=64, verbose_name="平台")
    mis_12 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="12mis的值")
    date = models.CharField(max_length=128, verbose_name="日期")

    class Meta:
        db_table = "mis12_platform_6DM"


class J6_Highway_Production_Month_12MIS(models.Model):
    Number_of_samples = models.IntegerField(verbose_name="索赔数量")
    date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="索赔日期")
    mis0 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="0mis的值", null=True, blank=True)
    mis1 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="1mis的值", null=True, blank=True)
    mis2 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="2mis的值", null=True, blank=True)
    mis3 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="3mis的值", null=True, blank=True)
    mis4 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="4mis的值", null=True, blank=True)
    mis5 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="5mis的值", null=True, blank=True)
    mis6 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="6mis的值", null=True, blank=True)
    mis7 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="7mis的值", null=True, blank=True)
    mis8 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="8mis的值", null=True, blank=True)
    mis9 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="9mis的值", null=True, blank=True)
    mis10 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="10mis的值", null=True, blank=True)
    mis11 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="11mis的值", null=True, blank=True)
    mis12 = models.DecimalField(decimal_places=1, max_digits=24, verbose_name="12mis的值", null=True, blank=True)
    Statistics_month = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="统计日期")

    class Meta:
        db_table = "J6_Highway_Production_Month_12MIS"


# todo 临时数据库，后期改善
class Frequency_of_claims_by_car_type(models.Model):
    date_of_claim = models.CharField(max_length=32, verbose_name="索赔日期")
    frequency = models.IntegerField(verbose_name="索赔频次")
    car_type = models.CharField(max_length=32, verbose_name="车型")
    platform = models.CharField(max_length=64, verbose_name="平台")
    let = models.CharField(max_length=32, verbose_name="排放")
    purpose = models.CharField(max_length=32, verbose_name="用途")

    class Meta:
        db_table = "Frequency_of_claims_by_car_type"
