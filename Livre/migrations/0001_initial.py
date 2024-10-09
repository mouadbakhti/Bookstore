# Generated by Django 5.0 on 2024-01-05 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discription', models.TextField(blank=True, null=True)),
                ('image_covr', models.ImageField(null=True, upload_to='photos/%y/%m/%d')),
                ('quantite', models.IntegerField()),
                ('pages', models.PositiveSmallIntegerField()),
                ('category', models.CharField(choices=[('Physique', 'Physique'), ('Mathématique', 'Mathématique'), ('Chimie', 'Chimie'), ('Science', 'Science'), ('Enfant', 'Enfant'), ('Informatique', 'Informatique')], max_length=190, null=True)),
                ('date_edition', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
