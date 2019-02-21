from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.

# BOOK MODEL
class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    publishDate = models.DateField(default="2019-02-21")

    def __str__(self):
        return self.name

#CAR MODEL
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.DateField(default='2019-21-02')

    def __str__(self):
        return self.make