from django.urls import path, include
from chart import views

urlpatterns = [
    path('bottom/', views.bottom, name="bottom_chart"),
]
