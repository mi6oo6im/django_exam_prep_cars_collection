from django.urls import path
from django_exam_prep_cars_collection.car.views import show_car_details, create_car, edit_car, delete_car

urlpatterns = (
    path('create/', create_car, name='create car'),
    path('<int:pk>/details/', show_car_details, name='car details'),
    path('<int:pk>/edit/', edit_car, name='edit car'),
    path('<int:pk>/delete/', delete_car, name='delete car'),
)
