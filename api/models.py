from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Item(models.Model):
    quantity = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["id"]