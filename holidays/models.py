# from pyexpat import model
from django.db import models

from django import forms

class HolidayRef(models.Model):
    ref = models.IntegerField()
    
class Continents(models.Model):
    continents = models.CharField(max_length =100)
    ref = models.ManyToManyField(HolidayRef)
    
    def __str__(self):
        return self.continents

class Countries(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    continents = models.ManyToManyField(Continents)
    countrie = models.CharField(max_length =100)

    def __str__(self):
        return self.continents, self.countrie

class Location(models.Model):
    ref = models.ManyToManyField(Countries)

class TypeHoliday(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    loaction = models.ManyToManyField(Location)
    type_hol = models.CharField(max_length =100)
    temp = models.CharField(max_length =100)

    def __str__(self):
        return (f'types is hoildays {self.type_hol} ')


class Holiday(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    type_hol = models.ManyToManyField(TypeHoliday)
    loaction = models.ManyToManyField(Location)
    HotelName = models.CharField(max_length =100)
    Area = models.CharField(max_length =100)
    StarRating = models.CharField(max_length =100)
    Location = models.CharField(max_length =100)
    PricePerPerNight = models.CharField(max_length =100)
    
    def __str__(self):
        return(f"{self.HotelName}, {self.Area}, {self.Location}, {self.PricePerPerNight}")
