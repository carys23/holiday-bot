from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.continent, name="continent"),
    path('asia/', views.asia, name="asia"),
    path('australia/', views.australia, name="australia"),
    path('antarctica/', views.antarctica, name="antarctica"),
    path('africa/', views.africa, name="africa"),
    path('europe/', views.europe, name="europe"),
    path('north_america/', views.north_america, name="north_america"),
    path('type_hol/<country>', views.type_hol, name="type_hol"),
    path('typeHoliday/<country>/<type_hol>', views.typeHoliday, name="typeHoliday"),
]