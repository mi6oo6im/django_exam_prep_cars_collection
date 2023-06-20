from django.forms import ModelForm, EmailInput, PasswordInput, TextInput
from django_exam_prep_cars_collection.car_profile.models import CarProfile


# Create forms here:
class BaseProfileForm(ModelForm):
    class Meta:
        model = CarProfile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'email': EmailInput,
            'password': PasswordInput,
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    BaseProfileForm.Meta.fields.extend(['first_name', 'last_name', 'profile_picture'])
    BaseProfileForm.Meta.widgets['password'] = TextInput


class DeleteProfileForm(BaseProfileForm):
    pass
