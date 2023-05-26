from django.db import models

from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
        ('en_attente', 'En attente'),
    )

    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente')

    def __str__(self):
        return self.titre
