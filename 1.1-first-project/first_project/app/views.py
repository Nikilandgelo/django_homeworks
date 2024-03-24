from datetime import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.now()
    return HttpResponse(f'Текущее время: {current_time}')

def workdir_view(request):
    list_files = os.listdir()
    return HttpResponse(f"{file}<br>" for file in list_files)