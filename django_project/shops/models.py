from django.db import models

from categories.models import Category


class Shop(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

