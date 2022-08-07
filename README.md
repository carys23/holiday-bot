# notes

* def get_countries_by_continent(continent):
    return Countries.objects.filter(continents__continents=continent)'
#### gets the arugument from the name within the models and the name in models from the foreignKey
<br>
<br>

* def australia(request):
    holiday = {"countries": get_countries_by_continent('Australia')}
    return render(request, 'australia.html', holiday)'

#### Then passes through the def get_countries_by_continent(continent) arugument 
<br>
<br>

* def type_hol(request, country):
    return render (request, 'type_hol.html', { 'country': country, 'holidays': TypeHoliday.objects.all()} )'
#### agrument of the country from url.py what button is clicked
<br>
<br>

* def typeHoliday(request, country, type_hol):    
    holiday = {"holidays": get_holiday_by_type_country_and_type(country, type_hol)}
    return render(request, 'holidays.html', holiday)'
#### 

* def get_holiday_by_type_country_and_type(country, type_hol):
    return Holiday.objects.filter(location__location__countries=country, type_hol__type_hol=type_hol)'

#### location_location_countries within Countries models is the argument with the url.py type_hol works the same way. Gets both contry and hol_type argument to then give the holidays avaible in the database


