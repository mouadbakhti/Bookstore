# Generated by Django 5.0 on 2024-01-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('datenaisance', models.DateField(null=True)),
                ('CNE', models.IntegerField()),
                ('section', models.CharField(max_length=40)),
            ],
        ),
    ]
