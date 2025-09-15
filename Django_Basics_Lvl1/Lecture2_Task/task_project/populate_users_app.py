import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_project.settings')

import django
django.setup()

## Fake top script
import random

from AppTwo.models import User
from faker import Faker

fakergen = Faker() 

def populateUsers(N=10):
  for i in range(N):
    fake_name = fakergen.name().split()
    fake_first_name = fake_name[0]
    fake_last_name = fake_name[1]
    fake_email = fakergen.email()
    users = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0];
    print(users);

if __name__ == '__main__':
  print("Populating the databases...Please Wait");
  populateUsers(20)
  print("Populated Users");