from django.contrib import admin

from .models import   Holiday, Countries, Location, TypeHoliday, Continents
admin.site.register(Holiday)
admin.site.register(Continents)
admin.site.register(Countries)
admin.site.register(Location)
admin.site.register(TypeHoliday)

