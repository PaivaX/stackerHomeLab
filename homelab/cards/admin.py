# public_ip_card/admin.py

from django.contrib import admin
from django import forms
from .models import Card

# Formulário personalizado para o Admin
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

    # Certifique-se de que 'data' não será obrigatório no formulário
    data = forms.JSONField(required=False, initial=dict)

class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'card_type', 'last_updated']
    form = CardForm  # Usar o formulário personalizado

admin.site.register(Card, CardAdmin)
