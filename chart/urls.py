from django.urls import path, include
from chart import views

urlpatterns = [
    path('bottom/bottomLeftChart/', views.bottomleftchart, name="bottom_chart"),
]
