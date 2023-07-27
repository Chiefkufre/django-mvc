from django.db import models
from django.conf import settings
from django.urls import reverse

import pint as ps

from datetime import datetime
# Create your models here.



User = settings.AUTH_USER_MODEL

from .utils import number_str_to_float
from .validators import validate_unit_of_measure

max_length=200
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=max_length, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    directions =  models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id})


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name  = models.CharField(max_length=max_length, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    quantity =  models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    # Remember to use pint as a unit of measurement
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated =  models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return self.recipe.get_absolute_url()
    
    def convert_to_system(self, system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg = ps.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg(self.unit)
        return measurement

    def as_mks(self):
        measurement = self.convert_to_system(system="mks")
        return measurement.to_base_units()
    

    def as_imperial(self):
        measurement = self.convert_to_system(system="imperial")
        return measurement.to_base_units()


    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)