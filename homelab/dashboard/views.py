from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cards.models import Card
from links.models import Link

@login_required
def index(request):
    cards = Card.objects.all()
    links = Link.objects.all()
    # Atualiza os dados dos cartões
    for card in cards:
        card.update_data()
        
    return render(request, 'index.html', {'cards': cards, 'links': links})

def layoutstatic(request):
    services = None
    return render(request, 'layout-static.html', {'services': services})


def login_view(request):
    return render(request, 'dashboard/login.html')