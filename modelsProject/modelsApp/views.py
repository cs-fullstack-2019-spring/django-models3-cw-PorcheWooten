# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
from .models import Book
from .models import Car


# CREATES NEW BOOK
def newBook(request):
    newObj = Book(name="A Child Called It", genre='fiction', publishDate='2000-01-02')
    newObj.save()
    return HttpResponse(newObj)


# show all books
def allBooks(request):
    allEntries = Book.objects.all()
    return HttpResponse(allEntries)


#filter's book by year
def greaterThan(request):
    objectsGreaterThanJan1 = Book.objects.filter(publishDate__gt='2018-01-01')
    return HttpResponse(objectsGreaterThanJan1)


# creates new car
def newCar(request):
    newObj = Car(make="Hyundai", model='Sonata', year='2016-1-02')
    newObj.save()
    return HttpResponse(newObj)

# show all cars
def allCars(request):
    allEnt = Car.year.objects.all()
    return HttpResponse(allEnt)
# filter's cars by year
def objGreaterThan(request):
    objGreater= Car.objects.filter(year__gt='2010-01-01')
    return HttpResponse(objGreaterThan)

