from django.shortcuts import render
from .models import Service
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    services = None
    return render(request, 'index.html', {'services': services})

def layoutstatic(request):
    services = None
    return render(request, 'layout-static.html', {'services': services})

def dash_index(request):
    services = Service.objects.all()
    return render(request, 'dashboard/dashboard.html', {'services': services})

def login_view(request):
    return render(request, 'dashboard/login.html')