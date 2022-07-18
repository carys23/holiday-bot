from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('countries/', views.countries, name="countries"),
    path('asia/', views.asia, name="asia"),
    path('australia/', views.australia, name="australia"),
    path('antarctica/', views.antarctica, name="antarctica"),
    path('africa/', views.africa, name="africa"),
    path('europe', views.europe, name="europe"),
    path('north_america/', views.north_america, name="north_america"),
    path('TypeHoliday/', views.TypeHoliday, name="hol-type"),
]