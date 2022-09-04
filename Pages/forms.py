from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import *

#create forms
class Opost(ModelForm):
    class Meta:
        model = Post
        fields = ('date','titre','image','description')
        

class Restauration(ModelForm):
    class Meta:
        model = resRestauration
        fields = ('Nom_Prenom','Email','Nbr_Personne','date','heure','Tel','status')


class Sport(ModelForm):
    class Meta:
        model = resSport
        fields = ('Nom_Prenom','Email','activite','date','heure','Tel','status')

class Rstatus(ModelForm):
    model = resRestauration
    fields = ('status')

class Sstatus(ModelForm):
    model = resSport
    fields = ('status')
 
