from django.db import models

# Create your models here.
class Livre(models.Model) :
    auteur = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=250, null=True)
    prix = models.CharField(max_length=100, null=True)

class Meta:
    db_table='stock'