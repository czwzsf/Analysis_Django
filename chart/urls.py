from django.urls import path, include
from chart import views

urlpatterns = [
    path('bottom/', views.bottom, name="bottom_chart"),
    path('bottom/', views.center, name="center_chart"),
    path('bottom/', views.centerLeft, name="centerLeft_chart"),
    path('bottom/', views.centerRight, name="centerRight_chart"),
]
