from django.urls import path

from django_exam_prep_cars_collection.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
