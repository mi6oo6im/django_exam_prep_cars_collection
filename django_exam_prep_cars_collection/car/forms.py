from django.forms import ModelForm
from django_exam_prep_cars_collection.car.models import Car


# Create forms here:
from django_exam_prep_cars_collection.car_profile.forms import BaseProfileForm


class BaseCarForm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        labels = {
            'image_url': "Image URL",
        }


class CarCreate(BaseCarForm):
    pass


class EditCar(BaseCarForm):
    pass


class DeleteCar(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

