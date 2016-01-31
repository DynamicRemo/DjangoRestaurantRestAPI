from django.contrib.auth.models import User
from django.db import models

from django.core.validators import validate_slug
from restaurantapi.validators import validate_acceptable_cost_to_make

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=200)
    chef = models.ForeignKey(User)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=32, unique=True, validators=[validate_slug])
    description = models.CharField(max_length=200)
    cost_to_make = models.DecimalField(decimal_places=2, max_digits=5, validators=[validate_acceptable_cost_to_make])
    sale_price = models.DecimalField(decimal_places=2, max_digits=5)
    available = models.BooleanField(default=False)
    menu = models.ForeignKey(Menu)

    def __str__(self):
        return self.name