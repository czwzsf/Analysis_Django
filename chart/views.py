from django.http import JsonResponse
from chart.models import Product_last_month_12mis, Product_id, E6_platform_mis, mis12_platform_6DM, \
    part_claim_mis, J6_Highway_Production_Month_12MIS, Frequency_of_claims_by_car_type


# Create your views here.


def bottomleftchart(request):
    cdata = {
        'Number_of_samples': [],
        'date': [],
        'mis3': [],
        'mis6': [],
        'mis9': [],
        'mis12': [],
        'date_s': []
    }
    queryset = J6_Highway_Production_Month_12MIS.objects.all()
    for item in queryset:
        cdata['Number_of_samples'].append(item.Number_of_samples)
        cdata['date'].append(item.date)
        cdata['mis3'].append(item.mis3)
        cdata['mis6'].append(item.mis6)
        cdata['mis9'].append(item.mis9)
        cdata['mis12'].append(item.mis12)
        cdata['date_s'].append(item.date_s)
    return JsonResponse(cdata)


def bottomrightchart(request):
    cdata = {
        'mis_data': [],
        'mis_12_1': [],
        'mis_12_2': [],
        'mis_12_3': [],
        'mis_12_4': [],
        'mis_12_5': [],
        'mis_12_6': [],
        'mis_12_7': [],
        'mis_12_8': [],
        'mis_12_9': [],
        'mis_12_10': [],
        'mis_12_11': [],
    }
    # 提取最近月
    queryset1 = Product_last_month_12mis.objects.filter(product_id_id__exact=1)
    for item in queryset1:
        cdata['mis_data'].append(item.mis_data)
    cdata['mis_data'] = sorted(list(set(cdata['mis_data'])))
    for i in range(Product_id.objects.all().count() + 1):
        queryset = Product_last_month_12mis.objects.filter(product_id_id__exact=i)
        for item in queryset:
            cdata['mis_12_' + str(i)].append(item.mis_12)
    return JsonResponse(cdata)


def leftoneChart(request):
    """
    左一图接口
    :param request:
    :type request:
    :return: 国六J6最近月12mis
    :rtype: json
    """
    cdata = {
        'data_mis': [],
        'mis_12': [],
    }
    queryset = E6_platform_mis.objects.all()
    for item in queryset:
        cdata['data_mis'].append(item.data_mis)
        cdata['mis_12'].append(item.mis_12)
    return JsonResponse(cdata)


def lefttwoChart(request):
    """
    # 左二图6DM各平台最近月mis
    :param request:
    :type request:
    :return:6DM各平台最近月mis
    :rtype:json
    """
    cdata = {
        "platform": [],
        "mis_12": [],
    }
    queryset = mis12_platform_6DM.objects.all()
    for item in queryset:
        cdata["platform"].append(item.platform)
        cdata["mis_12"].append(item.mis_12)
    return JsonResponse(cdata)


def righoneChart(request):
    cdata = {
        "part_name": [],
        "base_value": [],
        "current_value": [],
        "chain_ration": [],
        "year_on_year": []
    }
    queryset = part_claim_mis.objects.all()
    for item in queryset:
        cdata["part_name"].append(item.part_name)
        cdata["base_value"].append(item.base_value)
        cdata["current_value"].append(item.current_value)
        cdata["chain_ration"].append(item.chain_ratio)
        cdata["year_on_year"].append(item.year_on_year)
    return JsonResponse(cdata)


def bottomCenterChart(request):
    cdata = {
        'frequency': [],
        'date_of_claim': []
    }
    queryset = Frequency_of_claims_by_car_type.objects.filter(car_type__exact="J6", platform__exact="6DM2|6DM3",
                                                              let__exact="E5|E6")
    for item in queryset:
        cdata['frequency'].append(item.frequency)
        cdata['date_of_claim'].append(item.date_of_claim)
    return JsonResponse(cdata)
