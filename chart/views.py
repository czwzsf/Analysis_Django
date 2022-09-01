from django.http import JsonResponse
from chart.models import bottomLeftChart


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
