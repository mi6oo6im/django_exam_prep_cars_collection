from django.db import models

# Create your models here.

"""
•	Car

o	"Type"
	    Character (choice) field, required.
	    It should consist of a maximum of 10 characters.
	    The choices are "Sports Car", "Pickup", "Crossover", "Minibus" and "Other".
o	"Model"
	    Character field, required.
	    It should consist of a maximum of 20 characters.
	    It should consist of a minimum of 2 characters.
o	"Year"
	    Integer field, required.
	    Valid year is a year between 1980 and 2049 (both inclusive). Otherwise, raise a ValidationError with the message: "Year must be between 1980 and 2049"
o	"Image Url"
	    URL field, required.
o	"Price"
	    Float field, required.
	    Price cannot be below 1.	

"""