from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from phones.models import Phone


def index(request):
    return redirect(reverse('catalog'))

def show_catalog(request) -> HttpResponse:
    sort:str = request.GET.get("sort", "name")
    if sort.endswith("_desk"):
        sort = '-' + sort.replace("_desk", '')
    
    context = {
        'phones': Phone.objects.all().order_by(sort),
    }
    return render(request, 'catalog.html', context)

def show_product(request, slug) -> HttpResponse:
    context = {
        "phone": Phone.objects.filter(slug = slug)[0],
        'path_back': reverse('catalog')
    }
    return render(request, 'product.html', context)