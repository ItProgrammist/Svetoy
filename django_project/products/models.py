from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(
        to=Category,
        related_name='products',
        on_delete=models.CASCADE,
    )
