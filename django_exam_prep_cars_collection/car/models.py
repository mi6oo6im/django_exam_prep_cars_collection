from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
from django_exam_prep_cars_collection.car.validators import year_range_validator


class Car(models.Model):
    CAR_TYPES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )
    type = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=CAR_TYPES,
    )
    model = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(2),
        )
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            year_range_validator,
        )
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(1),
        )
    )
