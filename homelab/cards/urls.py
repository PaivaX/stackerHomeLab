from django.urls import path
from . import views
from . import utils

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('get_server_resources/', utils.get_server_resources, name='get_server_resources'),
]

