from django.core.exceptions import ValidationError
from datetime import date


def validate_date_schedule(value):
    if date.today() > value:
        raise ValidationError("Não é possível adicionar uma data anterior ao dia atual!")
    else:
        return value
