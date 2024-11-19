from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('layout-static/', views.layoutstatic, name='layout-static'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),
]
