# from pyexpat import model

from django.db import models

from django import forms
    
class Continents(models.Model):
    continents = models.CharField(max_length =100)
    def __str__(self):
        return self.continents


class Countries(models.Model):
    continents = models.ForeignKey(Continents, on_delete=models.CASCADE)
    countries = models.CharField(max_length =100)
    def __str__(self):
        return self.countries

class Location(models.Model):
    location = models.ForeignKey(Countries, on_delete=models.CASCADE)
    name = models.CharField(max_length =100)


class TypeHoliday(models.Model):
    type_hol = models.CharField(max_length =100)
    def __str__(self):
        return self.type_hol

class Temperature(models.Model):
    temperature = models.CharField(max_length =100)
    def __str__(self):
        return self.temperature


class Holiday(models.Model):
    type_hol = models.ForeignKey(TypeHoliday, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hotelName = models.CharField(max_length =100)
    area = models.CharField(max_length =100)
    satarRating = models.CharField(max_length =100)
    pricePerPerNight = models.CharField(max_length =100)
    
    def __str__(self):
        return(f"{self.hotelName}, {self.area}, {self.area}, {self.pricePerPerNight}")
