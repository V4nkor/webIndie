# Generated by Django 4.2.2 on 2023-06-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('idEditeur', models.AutoField(primary_key=True, serialize=False)),
                ('nomEditeur', models.CharField(max_length=80, verbose_name='le nom de cet editeur')),
            ],
        ),
        migrations.CreateModel(
            name='Jeu',
            fields=[
                ('idJeu', models.AutoField(primary_key=True, serialize=False)),
                ('nomJeu', models.CharField(max_length=80, verbose_name='le nom de ce jeu')),
                ('sortieJeu', models.DateField(verbose_name='la date de sortie de ce jeu')),
                ('prixJeu', models.FloatField(verbose_name='le prix de ce jeu')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('idStudio', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]