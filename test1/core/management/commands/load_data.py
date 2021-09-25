import random
import datetime
from django.core.management.base import BaseCommand
from core.models import *

authors = ['jack','bing','dave','saturn','ruby']
categories = ['Sport','Music','Love','Emo','Life style']


def generate_author():
    index = random.randint(0,4)
    return authors[index]

def generate_category():
    index = random.randint(0,4)
    return categories[index]

def generate_dates():
    year = random.randint(2000,2020)
    month = random.randint(1,12)
    day = random.randint(1,28)
    date = datetime.date(year,month,day)
    return date

def generate_reviews():
    number = random.randint(0,1)
    if number==0:
        return False 
    else:
        return True 


def generate_views():
    return random.randint(1,100)


class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.add_argument('music_data',type=str,help='music data file contains titles')
    
    def handle(self, *args, **kwargs):
        file_name = kwargs['music_data']
        with open(f'{file_name}.txt') as file:
            for row in file:
                title = row 
                author_name = generate_author()
                categories = generate_category()
                publish_date = generate_dates()
                views = generate_views()
                reviews = generate_reviews()

                # here is constructing models 
                author = Author.objects.get_or_create(name=author_name)
                journal = Journal(title=title,author=Author.objects.get(name=author_name),publish_date=publish_date,views=views,reviewed=reviews)
                    # category can't be defined unless there is a journal 
                journal.save()  # the save here because before adding the cateogry this must have an id. 
                category = JournalCategory.objects.get_or_create(name=categories)
                journal.category.add(JournalCategory.objects.get(name=categories))
                
    
        self.stdout.write(self.style.SUCCESS('Journals has be loaded successfully '))



