from django.db import models


class Item(models.Model):
    name = models.TextField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2)
