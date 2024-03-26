from csv import DictReader
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

class Csv_data():
    def __init__(self) -> None:
        self.paginator = ''
    def create_objects_list(self):
        with open(settings.BUS_STATION_CSV, "r", encoding='UTF-8') as csv_file:
            self.paginator = Paginator([{'Name': dict_.get("Name"), 'Street': dict_.get("Street"), 'District': dict_.get("District")}
                                        for dict_ in DictReader(csv_file)], 10)
    def get_objects_list(self, page_number: int):
        return self.paginator.get_page(page_number)

csv_data = Csv_data()

def index(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    csv_data.create_objects_list()
    return redirect(reverse('bus_stations'))

def bus_stations(request) -> HttpResponse:
    page_counter = int(request.GET.get("page", 1))
    current_page = csv_data.get_objects_list(page_counter)

    context = {
        'bus_stations': current_page.object_list,
        'page': current_page,
    }
    return render(request, 'stations/index.html', context)
