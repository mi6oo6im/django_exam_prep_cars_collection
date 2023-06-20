from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class CarProfile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(
            MinLengthValidator(2, "The username must be a minimum of 2 chars")
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
