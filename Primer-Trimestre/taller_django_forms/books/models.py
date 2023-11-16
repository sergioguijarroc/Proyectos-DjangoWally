from django.db import models
from django.core.validators import MaxValueValidator

class Book(models.Model):
    title=models.CharField(max_length=1000)
    author=models.CharField(max_length=200)
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    resume=models.TextField()
    created_at=models.TimeField(auto_now=True)
    updated_at=models.TimeField(auto_now_add=True)

def __str__(self):
    return self.title
# Create your models here.
