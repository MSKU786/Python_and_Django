import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_project.settings')

import django
django.setup()

## Fake top script
import random
from task_project.models import Users
from faker import Faker

fakergen = Faker() 

def populate(10):
  for i in range(N):
    fake_first_name = fakergen.first_name();
    fake_last_name = fakergen.last_name();
    fake_email = fakergen.email();
    users = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0];

if __name__ == '__main__':
  print("Populating the databases...Please Wait");
  populate(20)
  print("Populated Users");