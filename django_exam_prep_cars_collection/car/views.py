from django.shortcuts import render, redirect, get_object_or_404
from django_exam_prep_cars_collection.car.forms import CarCreate, EditCar, DeleteCar

# Create your views here.
from django_exam_prep_cars_collection.car.models import Car


def show_car_details(request, pk):
    current_car = get_object_or_404(Car, pk=pk)

    context = {
        'car': current_car
    }

    return render(request, 'car/car-details.html', context)


def create_car(request):
    form = CarCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'car/car-create.html', context)


def edit_car(request, pk):
    current_car = get_object_or_404(Car, pk=pk)
    form = EditCar(request.POST or None, instance=current_car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': current_car,
    }

    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    current_car = get_object_or_404(Car, pk=pk)
    form = DeleteCar(request.POST or None, instance=current_car)
    if request.method == 'POST':
        current_car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': current_car,
    }

    return render(request, 'car/car-delete.html', context)
