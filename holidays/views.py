from typing import Type
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

from .models import Holiday, Continents , Countries, TypeHoliday, Location


def login(request):
    return render(request, 'login.html', {})

def get_countries_by_continent(continent):
    return Countries.objects.filter(continents__continents=continent)

def continent(request):
    holiday = {"continent": Continents.objects.all()}
    return render (request, 'continent.html', holiday )

def countries(request):
    holiday = {"countries": Countries.objects.all()}

    return render (request, 'countries.html', holiday )

def australia(request):
    holiday = {"countries": get_countries_by_continent('Australia')}
    return render(request, 'australia.html', holiday)
    
def asia(request):
    holiday = {"countries": get_countries_by_continent('Asia')}
    return render(request, 'asia.html', holiday)

def north_america(request):
    holiday = {"countries": get_countries_by_continent('North America')}
    return render(request, 'north_america.html', holiday)

def antarctica(request):
    holiday = {"countries": get_countries_by_continent('Antarctica')}
    return render(request, 'antarctica.html', holiday)

def europe(request):
    holiday = {"countries": get_countries_by_continent('Europe')}
    return render(request, 'europe.html', holiday)

def africa(request):
    holiday = {"countries": get_countries_by_continent('Africa')}
    return render (request, 'africa.html', holiday )

def TypeHoliday(request):
    if request.method == 'POST':
        form = TypeHoliday(request.POST or None)

        if form.is_valid():
            form.save()
            holiday = {"TypeHoliday": TypeHoliday.objects.all()}
            return render (request, 'hol-type.html', holiday )

    else:
        holiday = {"TypeHoliday": TypeHoliday.objects.all()}
        return render (request, 'hol-type.html', holiday )
