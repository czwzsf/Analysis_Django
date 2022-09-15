from django.urls import path, include
from chart import views

urlpatterns = [
    # 国六j6生产月mis信息
    path('bottom/bottomLeftChart/', views.bottomleftchart, name="bottom_leftchart"),
    # 右下角图表
    path('bottom/bottomrightChart/', views.bottomrightchart, name="bottom_rightchart"),
    # 国六J6公路12mis
    path('centerLeft/leftoneChart/', views.leftoneChart, name="left_one_Chart"),
    # 6DM各平台最近月12MIS
    path('centerLeft/lefttwoChart/', views.lefttwoChart, name="left_two_Chart"),
    # 零部件12mis信息
    path('centerRight/rightoneChart/', views.righoneChart, name="right_one_Chart"),
    # 6DM车型索赔频次
    path('bottom/bottomCenterChart/', views.bottomCenterChart, name="bottom_center_chart")

]
