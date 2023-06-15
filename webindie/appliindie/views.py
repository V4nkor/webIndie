from django.shortcuts import render
from appliindie.models import *
from appliindie.forms import *
# Create your views here.
def accueil(request):
    return render(request, "appliindie/accueil.html")

def jeux(request):
    lesJeux = Jeu.objects.all()
    return render(request, "appliindie/jeux.html", {"jeux" : lesJeux } )

def jeu(request, jeu_id):
    formulaire = AvisForm()
    leJeu = Jeu.objects.get(idJeu = jeu_id)  
    avis = Avis.objects.filter(jeu = jeu_id)
    listeAvis = []
    for avi in avis :
        listeAvis.append({"commentaire" : avi.commentaire, "note" : avi.note})
    return render(request, "appliindie/jeu.html",{"jeu" : leJeu,"liste" : listeAvis,"composition" : avis,"form" : formulaire})

def formulaireCreationJeu(request):
    formulaire = JeuForm()
    return render(request, "appliindie/formulaireCreationJeu.html",{"form" : formulaire})

def creerJeu(request):
    form = JeuForm(request.POST)
    if form.is_valid() :
        nomJeu = form.cleaned_data['nomJeu']
        sortieJeu = form.cleaned_data['sortieJeu']
        prixJeu = form.cleaned_data['prixJeu']
        jeu = Jeu()
        jeu.nomJeu = nomJeu
        jeu.sortieJeu = sortieJeu
        jeu.prixJeu = prixJeu
        jeu.save()
        return render(request,"appliindie/traitementFormulaireCreationJeu.html",{"nom" : nomJeu})
    else :
        return render(request,"appliindie/traitementFormulaireCreationJeu.html",{"nom" : None})

def ajouterAvisAuJeu(request):
    return render(request, "appliindie/accueil.html")

def supprimerAvisAuJeu(request):
    return render(request, "appliindie/accueil.html")

def supprimerJeu(request):
    return render(request, "appliindie/accueil.html")

def afficherFormulaireModificationJeu(request):
    return render(request, "appliindie/accueil.html")

def modifierJeu(request):
    return render(request, "appliindie/accueil.html")

def avis(request):
    return render(request, "appliindie/accueil.html")

def avi(request):
    return render(request, "appliindie/accueil.html")

def editeurs(request):
    return render(request, "appliindie/accueil.html")

def editeur(request):
    return render(request, "appliindie/accueil.html")

def formulaireCreationEditeur(request):
    return render(request, "appliindie/accueil.html")

def creerEditeur(request):
    return render(request, "appliindie/accueil.html")

def supprimerEditeur(request):
    return render(request, "appliindie/accueil.html")

def afficherFormulaireModificationEditeur(request):
    return render(request, "appliindie/accueil.html")

def modifierEditeur(request):
    return render(request, "appliindie/accueil.html")

def studios(request):
    return render(request, "appliindie/accueil.html")

def studio(request):
    return render(request, "appliindie/accueil.html")

def formulaireCreationStudio(request):
    return render(request, "appliindie/accueil.html")

def creerStudio(request):
    return render(request, "appliindie/accueil.html")

def supprimerStudio(request):
    return render(request, "appliindie/accueil.html")

def afficherFormulaireModificationStudio(request):
    return render(request, "appliindie/accueil.html")

def modifierStudio(request):
    return render(request, "appliindie/accueil.html")