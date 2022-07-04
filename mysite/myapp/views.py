from django.shortcuts import render

from django.urls import reverse

from .models import Fruits


def myfunction(request):
    fruits = Fruits.objects.all()
    return render(request, 'base.html', {'base': fruits})


def main(request, raqam):
    base = Fruits.objects.get(id=raqam)
    return render(request, 'main.html', {'base': base})
