from django.urls import path
from . import views
from . import cards

urlpatterns = [
    path('', views.index, name='index'),
    path('layout-static/', views.layoutstatic, name='layout-static'),
    path('dashboards/', cards.dashboards, name='dashboards'),
]
