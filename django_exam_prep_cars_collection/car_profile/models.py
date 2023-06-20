from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
from django_exam_prep_cars_collection.car.models import Car


class CarProfile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(
            MinLengthValidator(2, "The username must be a minimum of 2 chars"),
        ),
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(18),
        )
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return (self.first_name + " " + self.last_name).strip()

        return ''
    
    @property
    def total_price(self):
        return sum(car.price for car in Car.objects.all())
