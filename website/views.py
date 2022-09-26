from django.shortcuts import render
from .models import Service


def massage(request):
    service = Service.objects.all()
    return render(request, 'website/main.html', {'service': service})


def eyelashes(request):
    service = Service.objects.all()
    return render(request, 'website/main.html', {'service': service})


def registration(request):
    service = Service.objects.all()
    return render(request, 'website/registration.html')


# def price(request):
#     service = Service.objects.service()
#     price = Service.objects.price()
#     return render(request, 'website/main.html', {'price': [service, price]})
