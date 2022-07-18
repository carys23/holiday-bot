# from pyexpat import model
from django.db import models

from django import forms

class HolidayRef(models.Model):
    ref = models.IntegerField()
    
class Continents(models.Model):
    continents = models.CharField(max_length =100)
    
    def __str__(self):
        return self.continents

class Countries(models.Model):
    continents = models.ManyToManyField(Continents)
    countries = models.CharField(max_length =100)

    def __str__(self):
        return (f' location :  {self.countries} ')

class Location(models.Model):
    Location = models.ManyToManyField(Countries)
    def __str__(self):
        return (f' location : {self.Location}')

class TypeHoliday(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    loaction = models.ManyToManyField(Location)
    type_hol = models.CharField(max_length =100)
    temp = models.CharField(max_length =100)

    def __str__(self):
        return (f'types is hoildays {self.type_hol} location : {self.loaction}')


class Holiday(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    type_hol = models.ManyToManyField(TypeHoliday)
    loaction = models.ManyToManyField(Location)
    hotelName = models.CharField(max_length =100)
    area = models.CharField(max_length =100)
    atarRating = models.CharField(max_length =100)
    area = models.CharField(max_length =100)
    pricePerPerNight = models.CharField(max_length =100)
    
    def __str__(self):
        return(f"{self.hotelName}, {self.area}, {self.area}, {self.pricePerPerNight}")
