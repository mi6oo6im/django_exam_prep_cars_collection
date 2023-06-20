from django.urls import path
from django_exam_prep_cars_collection.car_profile.views import show_profile_details, create_profile, edit_profile, \
    delete_profile

urlpatterns = (
    path("create/", create_profile, name="create profile"),
    path("details/", show_profile_details, name="profile details"),
    path("edit/", edit_profile, name="edit profile"),
    path("delete/", delete_profile, name="delete profile"),
)
