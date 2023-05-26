import django
django.setup()

from model.seed import run
from tache.seed import seed_tasks

if __name__ == '__main__':
	run()
	seed_tasks()