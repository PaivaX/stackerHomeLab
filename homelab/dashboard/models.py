from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    status = models.CharField(max_length=50, default='Unknown')  # Ex.: Running, Down
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
