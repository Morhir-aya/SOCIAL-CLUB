import email
from sys import maxunicode
from django.db import models

# Create your models here.

class Post(models.Model):
    date = models.DateField()
    titre = models.CharField(max_length=500)
    image = models.ImageField(null=True,blank=True, upload_to='./img/posts')
    description = models.TextField()

class resRestauration(models.Model):
    sts = (
        ('Acceptée','Acceptée'),
        ('Refusée','Refusée'),
    )
    Nom_Prenom = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Nbr_Personne = models.IntegerField()
    date = models.DateField()
    heure = models.TimeField()
    Tel = models.IntegerField()
    typeres = models.CharField(max_length=100,default='Restauration')
    status = models.CharField(max_length=100, choices=sts, default='En cours de traitement')

class resSport(models.Model):
    act = (
        ('Football','Football'),
        ('Tennis','Tennis'),
        ('Natation','Natation'),
        ('Basket','Basket'),
        ('Salle de Sport','Salle de Sport'),
    )

    sts = (
        ('Acceptée','Acceptée'),
        ('Refusée','Refusée'),
    )
    Nom_Prenom = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    activite = models.CharField(max_length=100, choices=act)
    date = models.DateField()
    heure = models.TimeField()
    Tel = models.IntegerField()
    typeres = models.CharField(max_length=100,default='Activité sportif')
    status = models.CharField(max_length=100, choices=sts, default='En cours de traitement')
    

    