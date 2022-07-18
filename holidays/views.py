from typing import Type
from django.shortcuts import render
from .forms import ListForm
# Create your views here.
from django.http import HttpResponse

# from .models import Holiday, Continent , Countries, TypeHoliday, Location


def login(request):
    return render(request, 'login.html', {})

def countries(request):
    holiday = {"continent": Continent.objects.all()}
    return render (request, 'continent.html', holiday )

def countries(request):
    holiday = {"countries": Countries.objects.all()}

    return render (request, 'countries.html', holiday )

def australia(request):
    holiday = {"countries": Location.objects.all()}
    return render(request, 'australia.html', holiday)
    
def asia(request):
    holiday = {"countries": Location.objects.all()}
    return render(request, 'asia.html', holiday)

def north_america(request):
    holiday = {"countries": Location.objects.all()}
    return render(request, 'north_america.html', holiday)

def antarctica(request):
    holiday = {"countries": Location.objects.all()}
    return render(request, 'antarctica.html', holiday)

def europe(request):
    holiday = {"countries": Location.objects.all()}
    return render(request, 'europe.html', holiday)

def africa(request):
    holiday = {"countries": Location.objects.all()}

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
