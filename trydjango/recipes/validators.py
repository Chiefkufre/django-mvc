import pint
from pint.errors import UndefinedUnitError
from django.core.exceptions import ValidationError





# Remember to use pint as a unit of measurement
valid_unit_measurements = ['pounds', 'lbs', 'oz', 'grams']

def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry
    
    try:
        single_uinit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{value} is not a known unit of measurement")
    except:
        raise ValidationError(f"{value} is invalid")