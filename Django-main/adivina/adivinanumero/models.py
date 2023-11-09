from django.conf import settings
from django.db import models
from django.db.models import Model
class AdivinaNumero(models.Model):
    numero= models.CharField(max_length=200)
    description = models.TextField()
    done=models.BooleanField(default=False)
    
    def __str__(self):
        return self.description
