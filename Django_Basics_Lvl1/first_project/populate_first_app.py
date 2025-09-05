import os 

# Set the settings module for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')


import django
django.setup()

## Fake top script

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakerger = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
  