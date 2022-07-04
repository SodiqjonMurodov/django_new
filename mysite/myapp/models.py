from django.db import models
from django.urls import reverse


class Farmers(models.Model):
    name = models.CharField(max_length=255, blank=True)
    price = models.CharField(default=998, max_length=255, blank=True)
    kg = models.CharField(default=998, max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Fruits'

    def __str__(self):
        return self.name


class Fruits(models.Model):
    farmer = models.ForeignKey(Farmers, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main', kwargs={'raqam': self.id})



