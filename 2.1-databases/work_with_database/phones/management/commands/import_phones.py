from django.core.management.base import BaseCommand
from csv import DictReader
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='UTF-8') as csv_file:
            phones = DictReader(csv_file, delimiter=';')
            for dict_phones in phones:
                Phone.objects.create(name = dict_phones.get("name"), price = dict_phones.get("price"),
                                    image = dict_phones.get("image"), release_date = dict_phones.get("release_date"),
                                    lte_exists = dict_phones.get("lte_exists"), slug = slugify(dict_phones.get("name")))