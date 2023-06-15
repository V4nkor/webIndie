from django import forms
from django.forms import ModelForm
from appliindie.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class JeuForm(ModelForm) :
    #sortieJeu = forms.DateField(input_formats=["%d/%m/%Y"])

    class Meta :
        model = Jeu
        fields = ['nomJeu','prixJeu','sortieJeu']
        widgets = {
            'sortieJeu': DateInput(format=("%d/%m/%Y")) 
        }

#class JeuForm(forms.Form) :
#    nomJeu = forms.CharField(
#            label = 'Nom de ce jeu',
#            max_length = 50
#        )
#    prixJeu = forms.FloatField(
#            label = 'Prix de cet ingredient',
#        )
#    sortieJeu = forms.DateField(
#            label = 'Date de sortie de ce jeu',
#        )

class AvisForm(ModelForm) :
    class Meta :
        model = Avis
        fields = ['jeu','utilisateur','note','commentaire']

#class AvisForm(forms.Form) :
#    note = forms.DoubleField(
#            label = 'Note de cet avis',
#            max_length = 50
#        )
#    commentaire = forms.TextField(
#            label = 'Commentaire de cet avis',
#        )