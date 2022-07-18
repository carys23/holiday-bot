from django.contrib import admin
from django.urls import include, path
# from holidays import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('holidays.urls')),
    
]
