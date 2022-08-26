from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Currencies'


class Item(models.Model):
    quantity = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    price = models.PositiveIntegerField(
        default=2,
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ["id"]
