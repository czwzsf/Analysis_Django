from django.http import JsonResponse
from chart.models import bottomLeftChart, Product_last_month_12mis


# Create your views here.


def bottomleftchart(request):
    cdata = {
        'category': [],
        'lineData': [],
        'barData': [],
        'rateData': []
    }
    queryset = bottomLeftChart.objects.all()
    for item in queryset:
        cdata['category'].append(item.category)
        cdata['lineData'].append(item.lineData)
        cdata['barData'].append(item.barData)
        cdata['rateData'].append(item.barData / item.lineData)
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
    queryset = Product_last_month_12mis.objects.filter(product_line__exact='工程')
    for item in queryset:
        cdata['mis_data'].append(item.mis_data)
        cdata['mis_12_2'].append(item.mis_12)
    cdata['mis_data'] = sorted(list(set(cdata['mis_data'])))
    return JsonResponse(cdata)
