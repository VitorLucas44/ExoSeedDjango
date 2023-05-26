import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'votre_projet.settings')
django.setup()

from django.db import transaction
from django.contrib.auth.models import User
from tache.models import Task

fake = Faker()

@transaction.atomic
def seed_tasks(num_tasks):
    for _ in range(num_tasks):
        titre = fake.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
        description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
        date_echeance = fake.future_date(end_date='+30d')
        statut = fake.random_element(elements=('en_cours', 'terminee', 'en_attente'))

        task = Task(titre=titre, description=description, date_echeance=date_echeance, statut=statut)
        task.save()

if __name__ == '__main__':
    num_tasks = 10  # Specify the number of tasks you want to generate
    seed_tasks(num_tasks)
    print(f'{num_tasks} tasks seeded successfully.')
