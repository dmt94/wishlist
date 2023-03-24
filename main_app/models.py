from django.db import models
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.id})