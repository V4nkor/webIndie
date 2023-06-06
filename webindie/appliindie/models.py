from django.db import models

# Create your models here.
class Jeu(models.Model) :
    idJeu = models.AutoField(primary_key = True)
    nomJeu = models.CharField(max_length = 80, verbose_name = 'le nom de ce jeu')
    sortieJeu = models.DateField(verbose_name = 'la date de sortie de ce jeu')
    prixJeu = models.FloatField(verbose_name = 'le prix de ce jeu')

class Editeur(models.Model) :
    idEditeur = models.AutoField(primary_key = True)
    nomEditeur = models.CharField(max_length = 80, verbose_name = 'le nom de cet editeur')

class Edite(models.Model) :
    class Meta :
        unique_together = ('editeur','jeu')
    jeu = models.ForeignKey(Jeu, on_delete = models.CASCADE)
    editeur = models.ForeignKey(Editeur, on_delete = models.CASCADE)

class Studio(models.Model) :
    idStudio = models.AutoField(primary_key = True)
    nomStudio = models.CharField(max_length = 80, verbose_name = 'le nom de ce studio')

class Developpe(models.Model) :
    class Meta :
       unique_together = ('studio','jeu')
    jeu = models.ForeignKey(Jeu, on_delete = models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete = models.CASCADE)

class Utilisateur(models.Model) :
    idUtilisateur = models.AutoField(primary_key = True)
    pseudoUtilisateur = models.CharField(max_length = 80, verbose_name = 'le pseudo de l\'utilisateur')
    creationCompteUtilisateur = models.DateField()
    mdpUtilisateur = models.CharField()

class Avis(models.Model) :
    class Meta :
            unique_together = ('jeu','utilisateur')

    idAvis = models.AutoField(primary_key = True)

    jeu = models.ForeignKey(Jeu, on_delete = models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE)

    commentaire = models.TextField(verbose_name = 'le commentaire')
