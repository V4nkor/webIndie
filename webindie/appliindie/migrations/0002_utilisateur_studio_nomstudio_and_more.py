# Generated by Django 4.2.2 on 2023-06-07 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appliindie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('idUtilisateur', models.AutoField(primary_key=True, serialize=False)),
                ('pseudoUtilisateur', models.CharField(max_length=80, verbose_name="le pseudo de l'utilisateur")),
                ('creationCompteUtilisateur', models.DateField()),
                ('mdpUtilisateur', models.CharField(max_length=80, verbose_name="le mot de passe de l'utilisateur")),
            ],
        ),
        migrations.AddField(
            model_name='studio',
            name='nomStudio',
            field=models.CharField(default=None, max_length=80, verbose_name='le nom de ce studio'),
        ),
        migrations.AlterField(
            model_name='editeur',
            name='nomEditeur',
            field=models.CharField(default=None, max_length=80, verbose_name='le nom de cet editeur'),
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('idAvis', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.PositiveIntegerField()),
                ('commentaire', models.TextField(verbose_name='le commentaire')),
                ('jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliindie.jeu')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliindie.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Edite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliindie.editeur')),
                ('jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliindie.jeu')),
            ],
            options={
                'unique_together': {('editeur', 'jeu')},
            },
        ),
        migrations.CreateModel(
            name='Developpe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliindie.jeu')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliindie.studio')),
            ],
            options={
                'unique_together': {('studio', 'jeu')},
            },
        ),
        migrations.AddConstraint(
            model_name='avis',
            constraint=models.CheckConstraint(check=models.Q(('note__range', (0, 10))), name='appliindie_avis_note_range'),
        ),
    ]
