from django.shortcuts import render


# Create your views here.
from django_exam_prep_cars_collection.car.models import Car


def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request, 'common/catalogue.html', context)
