from django.urls import path, include
from chart import views

urlpatterns = [
    # 左下角图表
    path('bottom/bottomLeftChart/', views.bottomleftchart, name="bottom_leftchart"),
    # 右下角图表
    path('bottom/bottomrightChart/', views.bottomrightchart, name="bottom_rightchart")
]
