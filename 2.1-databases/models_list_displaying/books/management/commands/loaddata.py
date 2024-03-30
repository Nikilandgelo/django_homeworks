from django.core.management.base import BaseCommand
from json import load
from books.models import Book

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        with open("fixtures/books.json", "r", encoding='UTF-8') as json_file:
            for dict_ in load(json_file):
                Book.objects.create(name = dict_.get("fields").get("name"),
                                    author = dict_.get("fields").get("author"),
                                    pub_date = dict_.get("fields").get("pub_date"))