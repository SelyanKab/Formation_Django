from django.db import models

# Create your models here.
class Commande(models.Model):
    STATUS = (('en instance','en instance'),
            ('non livré','non livré'),
              ('livré','livré'))
    #client =
    #produit =
    status =models.CharField(max_length=200, numll=True,choices=SATUS)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
