from django.contrib import admin
from django.urls import path
from appliindie import views

urlpatterns = [
    path('', views.accueil),
    path('jeux/', views.jeux),
    path('jeu/<int:jeu_id>/', views.jeu),
    path('jeux/add/',views.formulaireCreationJeu),
    path('jeux/create/',views.creerJeu),
    path('jeux/<int:jeu_id>/addAvis/', views.ajouterAvisAuJeu),
    path('jeux/<int:jeu_id>/deleteAvis/<int:avis_id>/',views.supprimerAvisAuJeu),
    path('jeux/<int:jeu_id>/delete/',views.supprimerJeu),
    path('jeux/<int:jeu_id>/update/',views.afficherFormulaireModificationJeu),
    path('jeux/<int:jeu_id>/updated',views.modifierJeu),

    path('avis/', views.avis),
    path('avi/<int:avis_id>/', views.avi),
    
    path('editeurs/', views.editeurs),
    path('editeur/<int:editeur_id>/', views.editeur),
    path('editeurs/add/',views.formulaireCreationEditeur),
    path('editeurs/create/',views.creerEditeur),
    path('editeurs/<int:editeur_id>/delete/',views.supprimerEditeur),
    path('editeurs/<int:editeur_id>/update/',views.afficherFormulaireModificationEditeur),
    path('editeurs/<int:editeur_id>/updated',views.modifierEditeur),

    path('studios/', views.studios),
    path('studio/<int:studio_id>/', views.studio),
    path('studios/add/',views.formulaireCreationStudio),
    path('studios/create/',views.creerStudio),
    path('studios/<int:studio_id>/delete/',views.supprimerStudio),
    path('studios/<int:studio_id>/update/',views.afficherFormulaireModificationStudio),
    path('studios/<int:studio_id>/updated',views.modifierStudio)
]