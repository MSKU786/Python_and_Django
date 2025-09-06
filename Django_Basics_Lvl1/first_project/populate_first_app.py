import os 

# Set the settings module for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')


import django
django.setup()

## Fake top script

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakergen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
  t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
  t.save()
  return t

def populate(N=5):
  for entry in range(N):

    top = add_topic();

    #Genrate fake data for that entry
    fake_url = fakergen.url();
    fake_date = fakergen.date();
    fake_name = fakergen.company();

    #Create the new webpage entry
    webpage = Webpage.objects.get_or_create(topic = top, name = fake_name, urls = fake_url)[0];

    #Create a fake access record for that webpage
    acc_rec = AccessRecord.objects.get_or_create(name = webpage, date = fake_date)[0];


if __name__ == '__main__':
  print("Populating the databases...Please Wait");
  populate(20)
  print("Populating Complete");