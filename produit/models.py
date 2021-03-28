from django.db import models

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prix = models.FloatField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)