from django import template

from django_exam_prep_cars_collection.car_profile.models import CarProfile

register = template.Library()


@register.simple_tag
def get_profile_object():
    current_user = CarProfile.objects.first()
    return current_user
