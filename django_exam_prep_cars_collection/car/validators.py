from django.core.exceptions import ValidationError

valid_start_year = 1980
valid_end_year = 2049


def year_range_validator(value):
    if not (valid_start_year <= value <= valid_end_year):
        raise ValidationError(f"Year {value} must be between {valid_start_year} and {valid_end_year}")
