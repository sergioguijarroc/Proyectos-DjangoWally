from django.conf import settings
from django.db import models
from django.db.models import Model
class Comentarios(models.Model):
    nombre= models.CharField(max_length=200)
    email= models.EmailField()
    comentario=models.TextField()
    
    def __str__(self):
        return self.nombre
