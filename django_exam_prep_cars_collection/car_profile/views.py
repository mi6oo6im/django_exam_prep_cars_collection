from django.shortcuts import render, redirect

# Create your views here.
from django_exam_prep_cars_collection.car.models import Car
from django_exam_prep_cars_collection.car_profile.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from django_exam_prep_cars_collection.car_profile.models import CarProfile


def show_profile_details(request):
    return render(request, 'car_profile/profile-details.html')


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car_profile/profile-create.html', context)


def edit_profile(request):
    current_profile = CarProfile.objects.first()
    form = EditProfileForm(request.POST or None, instance=current_profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'car_profile/profile-edit.html', context)


def delete_profile(request):
    current_profile = CarProfile.objects.first()
    all_cars = Car.objects.all()
    if request.method == 'POST':
        current_profile.delete()
        all_cars.delete()
        return redirect('index')

    return render(request, 'car_profile/profile-delete.html')
