# cards/views.py

from django.shortcuts import render
from .models import Card

def dashboard(request):    
    # Obtém o cartão do tipo 'public_ip'
    ip_card = Card.objects.filter(card_type='public_ip').first()  # Pega o primeiro cartão 'public_ip'
    
    if ip_card:
        ip_card.update_data()  # Atualiza os dados do cartão com o IP público
    else:
        # Se não encontrar o cartão, pode ser interessante criar um novo ou exibir uma mensagem de erro
        ip_card = None
        
    return render(request, 'dashboard.html', {'ip_card': ip_card})