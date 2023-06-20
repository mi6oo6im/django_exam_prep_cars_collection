from django.urls import path

from django_exam_prep_cars_collection.common.views import index, catalogue

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
)
