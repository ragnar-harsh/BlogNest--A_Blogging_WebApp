from django.db import models

class contactModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    message = models.TextField()
# Create your models here.
