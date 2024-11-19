# cards/models.py
from django.db import models
from .utils import get_public_ip_info, get_docker_info

class Card(models.Model):
    name = models.CharField(max_length=200)
    card_type = models.CharField(max_length=100, choices=[('docker', 'Docker'), ('public_ip', 'Public IP')])
    frequency = models.IntegerField(default=30)  # Frequência em segundos, por exemplo
    data = models.JSONField(default=dict)
    last_updated = models.DateTimeField(auto_now=True)

    def update_data(self):
        if self.card_type == 'docker':
            self.data = get_docker_info()
        elif self.card_type == 'public_ip':
            self.data = get_public_ip_info()
        self.save()

    def __str__(self):
        return self.name
